#!/usr/bin/python
import logging
from Lib._RunnableObject import _RunnableObject
from Lib.ParameterChecking import checkType, checkAttr
from Protocol.GRPC.IEACP_pb2_grpc import add_AgentServicer_to_server
from Server import Server
from NCServicerImpl import NCServicerImpl

from Lib.ParameterChecking import checkType, checkAttr, checkString, checkIPv4
from Lib._Object import _Object
from Lib.Handlers.Callbacks import Callbacks as CallbacksHandler
from nodecontroller.RMON import Agent_RMON
from nodecontroller.SNMP import Agent_SNMP
from Lib._Configuration import _Configuration
from Lib.ParameterChecking import checkType, checkAttr, checkString
from nodecontroller._Agent import _Agent
from Lib.LoggerConfigurator import LoggerConfigurator
import sys, signal, logging, argparse, threading

from SendSample import SendSample



VERSION = '0.1.0'

class Manager(_RunnableObject,CallbacksHandler):
    CALLBACK_MESSAGE_STATISTICS = 'receivedMessageStatistics'
    CALLBACK_MESSAGE_HISTORY = 'receivedMessageHistory'
    CALLBACK_MESSAGE_ifTable = 'receivedMessageifTable'
    CALLBACK_MESSAGE_CPUS = 'receivedMessageCPUs'
    CALLBACK_MESSAGE_RAM = 'receivedMessageRAM'
    CALLBACK_MESSAGE_FLASH = 'receivedMessageFLASH'

    CALLBACK_KINDS = [
        CALLBACK_MESSAGE_STATISTICS,
        CALLBACK_MESSAGE_HISTORY,
        CALLBACK_MESSAGE_ifTable,
        CALLBACK_MESSAGE_CPUS,
        CALLBACK_MESSAGE_RAM,
        CALLBACK_MESSAGE_FLASH
    ]

    def __init__(self, terminate, exporter,templatesCatalog):
        _RunnableObject.__init__(self, 'Manager')
        self.__logger = logging.getLogger(__name__)
        self.__logger.info('Instantiating Manager...')
        self.__terminate = terminate
        self.__exporter = exporter
        self.__templatesCatalog = templatesCatalog
        self.__ieacp = Server([
            (NCServicerImpl(self), add_AgentServicer_to_server),
        ])
        CallbacksHandler.__init__(self, Manager.CALLBACK_KINDS)
        self._agentes = {}
        self._config = {}
        terminate = threading.Event()
        self._stopsignal = False
        self.__logger.debug("Init Manager")
        # initialize other entities belonging to the manager

    def __del__(self):
        if(self.isRunning()): self.stop()

    def getVersion(self):        return(VERSION)
    def getTerminateEvent(self): return(self.__terminate)

    @staticmethod
    def checkConfiguration(config):
        logger = logging.getLogger(__name__)
        logger.info('[Manager:checkConfiguration] begin')
        _RunnableObject.checkConfiguration(config)
        Server.checkConfiguration(checkAttr('ieacp', config))
        # check configuration of other entities belonging to the manager
        logger.info('[Manager:checkConfiguration] end')
    
    @staticmethod
    def getDefaultConfig():
        logger = logging.getLogger(__name__)
        logger.info('[Manager:getDefaultConfig] begin')
        defaultConfig = {
            'ieacp': Server.getDefaultConfig(),
            # get default configuration of other entities belonging to the manager
        }
        logger.info('[Manager:getDefaultConfig] end')
        return(defaultConfig)

    def getConfig(self):
        self.__logger.info('[Manager:getConfig] begin')
        config = {
            'ieacp': self.__ieacp.getConfig(),
            # get configuration of other entities belonging to the manager
        }
        self.__logger.info('[Manager:getConfig] end')
        return(config)

    def createagent(self,nameAgent, Type, IP, Port, mpModel):
        configuration = dict()
        configuration['deviceIP'] = IP
        configuration['devicePort'] = int(Port)
        configuration['mpModel'] = int(mpModel)
        if (Type == "rmon"):
            self._agentes[nameAgent] = Agent_RMON(self.__logger,self.__exporter,self.__templatesCatalog)
            self._agentes[nameAgent].configure(configuration)
            self.__logger.debug("Passing parameters to RMON agent ")
            self._agentes[nameAgent].registerCallback(Agent_RMON.CALLBACK_MESSAGE_STATISTICS,self.receiver)
            self._agentes[nameAgent].registerCallback(Agent_RMON.CALLBACK_MESSAGE_HISTORY,self.receiver)
            

        elif(Type == "snmp" ):
            self._agentes[nameAgent] = Agent_SNMP(self.__logger,self.__exporter,self.__templatesCatalog)
            self._agentes[nameAgent].configure(configuration)
            self.__logger.debug("Passing parameters to SNMP agent ")
            self._agentes[nameAgent].registerCallback(Agent_SNMP.CALLBACK_MESSAGE_ifTable,self.receiver)
            self._agentes[nameAgent].registerCallback(Agent_SNMP.CALLBACK_MESSAGE_CPUS,self.receiver)
            self._agentes[nameAgent].registerCallback(Agent_SNMP.CALLBACK_MESSAGE_RAM,self.receiver)
            self._agentes[nameAgent].registerCallback(Agent_SNMP.CALLBACK_MESSAGE_FLASH,self.receiver)
        return("Correct")
    def modifyagent(self, nameAgent, Type, IP, Port, mpModel):
    	configuration = dict()
        configuration['deviceIP'] = IP
        configuration['devicePort'] = int(Port)
        configuration['mpModel'] = int(mpModel)
    	
    	try:
    		aux = self._agentes[nameAgent]
    		self._agentes[nameAgent].configure(configuration)
    		return("All correct")
    	except:
    		return("Failed")
    def deleteagent(self, nameAgent):
    	d = self._agentes[nameAgent].getConfiguredObservationPoints()
    	for key in d.keys():
    		self.deleteop(nameAgent,key[0],key[1])
    	aux = self._agentes.pop(nameAgent, None)	
    	if aux is None:
    		return("Failed")
    	else:
    		return("All correct")

    def listagent(self):
    	return (self._agentes)

    def createop(self, nameAgent,  observationDomainId, observationPointId, componentId, componentType,templateId, monitoringPeriod):
        #Comprobamos si existe el op, si es asi devuelve false  y no configura el op
        self.__logger.debug("createop in Manager") 
        try:
            ops = self._agentes[nameAgent].getConfiguredObservationPoints(None,None)
            for key, value in ops.iteritems():
                if key[0] == observationDomainId:
                    if key[1] == observationPointId:
                        return("Created")
        
            ok = self._agentes[nameAgent].configureObservationPoint(int(observationDomainId), int(observationPointId),int(componentId), componentType,int(templateId),int(monitoringPeriod))
            if(ok is not None):
                self._agentes[nameAgent].deleteop(int(observationDomainId),int(observationPointId))
                return(ok)
            else:
                return("All Correct")

        except:
            self._agentes[nameAgent].deleteop(int(observationDomainId),int(observationPointId))
            return("Fail")
        

    def modifyop(self, nameAgent, observationDomainId, observationPointId,  componentId, componentType,templateId, monitoringPeriod):
        #Comprobamos si exite el ops, si es asi configura el op y devuelve true
        self.__logger.debug("Modifyop in Manager") 
        try:
            ops = self._agentes[nameAgent].getConfiguredObservationPoints(None,None)
            for key, value in ops.iteritems():
                if key[0] == observationDomainId:
                    if key[1] == observationPointId:
                        ok = self._agentes[nameAgent].configureObservationPoint(int(observationDomainId), int(observationPointId), int(componentId), componentType, int(templateId),int(monitoringPeriod))
                        if(ok is not None):
                            print "hello \n"
                            print ok
                            return(ok)
                        else:
                            return("All Correct")
                    
        except:
            return("Fail")
        return("Fail modify observation point")

    def deleteop(self, nameAgent, observationDomainId, observationPointId):
        return(self._agentes[nameAgent].deleteop(observationDomainId,observationPointId))

    def enableop(self, nameAgent, observationDomainId, observationPointId):
        return(self._agentes[nameAgent].enableop(observationDomainId,observationPointId))

    def disableop(self, nameAgent, observationDomainId, observationPointId):
        return(self._agentes[nameAgent].disableop(observationDomainId,observationPointId))

    def listop(self,observationDomainIdId = None,observationPointId=None):
        dicOp = dict()
        for agente,value in self._agentes.iteritems():
            dicOp[agente] = self._agentes[agente].getConfiguredObservationPoints(observationPointId,observationPointId)
        return(dicOp)

    def configure(self, config):
        self.__logger.info('Configuring Manager...')
        self.__logger.info('[Manager:configure] begin')
        _RunnableObject.configure(self, config)
        Manager.checkConfiguration(config)
        self.__ieacp.configure(config.get('ieacp'))
        # configure other entities belonging to the manager
        self.setConfigured()
        self.__logger.info('[Manager:configure] end')

       
    def startagents(self):
    	self.__logger.debug("startagents in Manager") 
        for agente,value in self._agentes.iteritems():
            self._agentes[agente].start()
        self._running = True
        
    
    def stopagents(self):
        self.__logger.debug("stopagents in Manager")
        for agente,value in self._agentes.iteritems():
            self._agentes[agente].stop()
        self._stopsignal = True

    def receiver(self,sample):
        self.__logger.debug ("Receveir in Manager")
        SendSample(self.__exporter,sample,self.__logger)
        

    def deconfigure(self):
        self.__logger.info('Deconfiguring Manager...')
        self.__logger.info('[Manager:deconfigure] begin')
        _RunnableObject.deconfigure(self)
        self.__ieacp.deconfigure()
        # deconfigure other entities belonging to the manager
        self.unsetConfigured()
        self.__logger.info('[Manager:deconfigure] end')

    def start(self):
        self.__logger.info('Starting Manager...')
        self.__logger.info('[Manager:start] begin')
        _RunnableObject.start(self)
        self.__ieacp.start()
        self.startagents()
        # start other entities belonging to the manager
        self.setRunning()
        self.__logger.info('[Manager:start] end')

    def stop(self):
        self.__logger.info('Terminating Manager...')
        self.__logger.info('[Manager:stop] begin')
        _RunnableObject.stop(self)
        self.__ieacp.stop()
        self.stopagents()
        # stop other entities belonging to the manager
        self.unsetRunning()
        self.__terminate.set()
        self.__logger.info('[Manager:stop] end')
