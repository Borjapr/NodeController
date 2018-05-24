from Lib.Handlers.Callbacks import Callbacks as CallbacksHandler
from Lib.ParameterChecking import checkType, checkAttr, checkString, checkIPv4,checkPort, checkValue
from nodecontroller.Samplers import SamplerFactory
from nodecontroller._Agent import _Agent
from nodecontroller.GetNext import getnext
from collections import defaultdict



class Agent_SNMP(_Agent,CallbacksHandler):

    CALLBACK_MESSAGE_ifTable = 'receivedMessageifTable'
    CALLBACK_MESSAGE_CPUS = 'receivedMessageCPUs'
    CALLBACK_MESSAGE_RAM = 'receivedMessageRAM'
    CALLBACK_MESSAGE_FLASH = 'receivedMessageFLASH'

    CALLBACK_KINDS_SNMP = [
        CALLBACK_MESSAGE_ifTable,
        CALLBACK_MESSAGE_CPUS,
        CALLBACK_MESSAGE_RAM,
        CALLBACK_MESSAGE_FLASH
    ]

    def __init__(self,log,ipfixExporter,templatesCatalog):
        _Agent.__init__(self, 'Agent_SNMP')
        CallbacksHandler.__init__(self, Agent_SNMP.CALLBACK_KINDS_SNMP)
        # initialize Agent_SNMP attributes
        self.__OP = defaultdict(dict)
        self._log = log
        self._ipfixExporter=ipfixExporter
        self._templatesCatalog = templatesCatalog
        self._observationpointlist =[]
        self._log.debug("Init in SNMP")
        self._enable = True
        

    @staticmethod
    def checkConfiguration(config):
        checkIPv4('deviceIP', checkAttr('deviceIP', config))
        checkPort('devicePort', checkAttr('devicePort', config))
        
    
    def configure(self, config):
        Agent_SNMP.checkConfiguration(config)
        # configure Agent_SNMP
        # config = dict({'deviceIP':<str>, 'devicePort':<int>, 'mpModel':<int>})
        #Load attributes
        self._deviceIP = checkAttr('deviceIP', config)
        self._devicePort = checkAttr('devicePort',config)
        self._mpModel = checkAttr('mpModel',config)
        self._configured = True
        self._log.debug("Configuration parameters SNMP Agent")
        self._log.debug(self._deviceIP)
        self._log.debug(self._devicePort)
        self._log.debug(self._mpModel)
        
    def start(self):
        self._log.debug("start in SNMP Agent")
        for key, opdata in self.__OP.iteritems():
            self.enableop(key[0],key[1])
        self._running = True

    def disableop(self,observationDomainId,observationPointId):
        self._log.debug("Disable in SNMP Agent")
        try: 
            self.__OP[(observationDomainId, observationPointId)]["sampler"].stop()
            self.__OP[(observationDomainId, observationPointId)]["enable"] = False
            return("All Correct")
        except:
            return("Fail")

    def enableop(self,observationDomainId,observationPointId):
        self._log.debug("enableop in SNMP Agent")
        try:
            self.__OP[(observationDomainId, observationPointId)]["sampler"].start()
            self.__OP[(observationDomainId, observationPointId)]["enable"] = True
            return("All correct")
        except:
            return("Fail")

    def stop(self):
        self._log.debug("stop in SNMP Agent")
        for key, opdata in self.__OP.iteritems():
            self.disableop(key[0],key[1])
        self._running = False

    def deleteop(self,observationDomainId,observationPointId):
        self._log.debug("Deleteop in SNMP Agent")
        self.disableop(observationDomainId, observationPointId)
        aux = self.__OP.pop((observationDomainId, observationPointId),None)
        if aux == None:
            return("Fail")
        else:
            return("All Correct")
        
    def configureObservationPoint(self, observationDomainId, observationPointId, componentId = None , componentType = None,
                                  templateId = None, monitoringPeriod = None):
        self._log.debug("Configure observationPoint in SNMP Agent: Configure Parameters")
        self._log.debug(observationPointId)
        self._log.debug(observationDomainId)
        self._log.debug(componentId)
        self._log.debug(componentType)
        self._log.debug(templateId)
        self._log.debug(monitoringPeriod)
        
        if (self.__OP.get((observationDomainId, observationPointId)) !=None ):
            self._log.debug("Modify op")
            if((componentType is not None) and (self.__OP[(observationDomainId, observationPointId)]['componentType'] != componentType)):
                raise Exception("Error componentType")
            self._log.debug("modifying sampler in SNMP")
            #Paramos timer
            self.__OP[(observationDomainId, observationPointId)]["sampler"].stop()
            self.__OP[(observationDomainId, observationPointId)]["enable"] = False

            #Actualizamos valores del ObservationPoint
            if(componentId is not None):
                self.__OP[(observationDomainId, observationPointId)]["componentId"] = componentId
                
            
            if(templateId is not None):
                self.__OP[(observationDomainId, observationPointId)]["templateId"] = templateId
                
            if(monitoringPeriod is not None):
                self.__OP[(observationDomainId, observationPointId)]["monitoringPeriod"] = monitoringPeriod


            #Actualizamos el exporter con la templateId y observationDomainId
            domain = (self._ipfixExporter.getSession()).getDomain(observationDomainId)     
            ok_domain = domain.hasExporterTemplate(templateId)  
            if (ok_domain == False):
                return("Domain has not this Template")  

            self._templatesCatalog.injectAllTemplates(self._ipfixExporter,obsDomainId=observationPointId, templateIds=[templateId])

            #Configuramos sampler
            self.__OP[(observationDomainId, observationPointId)]["sampler"].configure(monitoringPeriod,observationDomainId,observationPointId,templateId)

            #Iniciamos timer
            self.__OP[(observationDomainId, observationPointId)]["sampler"].start()
            self.__OP[(observationDomainId, observationPointId)]["enable"] = True


        else:
            if((componentType is  None) or (templateId is  None) or (monitoringPeriod is  None)):
                raise Exception("Error config parameters")
            self._log.debug("Creating Sampler in SNMP")
            #Configuramos ObservationPoint
            self.__OP[(observationDomainId, observationPointId)]["componentId"] = componentId
            self.__OP[(observationDomainId, observationPointId)]["componentType"] = componentType
            self.__OP[(observationDomainId, observationPointId)]["templateId"] = templateId
            self.__OP[(observationDomainId, observationPointId)]["monitoringPeriod"] = monitoringPeriod
            

            #Actualizamos el exporter con la templateId y observationPointId
            domain = (self._ipfixExporter.getSession()).getDomain(observationDomainId)     
            #ok_domain = domain.hasExporterTemplate(templateId)  
            #if (ok_domain == False):
            #    return("Domain has not this Template")

            self._templatesCatalog.injectAllTemplates(self._ipfixExporter,obsDomainId=observationDomainId, templateIds=[templateId])

            self._log.debug("Sampler Factory in SNMP Agent")
            #Creamos un sampler
            self.__OP[(observationDomainId, observationPointId)]["sampler"]=SamplerFactory.get(componentType,self)
            self._log.debug("configurating sampler in SNMP")

            #Configuramos sampler
            ok = self.__OP[(observationDomainId, observationPointId)]["sampler"].configure(monitoringPeriod,observationDomainId,observationPointId,templateId)
            if(ok is not None):
                return(ok)

            self._log.debug("Starting sampler in SNMP")
            #Iniciamos sampler
            try:
                self.__OP[(observationDomainId, observationPointId)]["sampler"].start()
                self.__OP[(observationDomainId, observationPointId)]["enable"] = True
            except:
                self.deleteop((observationDomainId, observationPointId))
                pass




 
    def getConfiguredObservationPoints(self,observationDomainId = None,observationPointId = None):
        self._log.debug("In getConfigureObservationPoints")
        if((observationDomainId is not None) and (observationPointId is not None)):
            return(self.__OP[(observationDomainId, observationPointId)])
        else:
            return(self.__OP)  

    def getSerialNumber(self):
        #1.3.6.1.4.1.17.1.12.1.1.12.0 agent serial number
        MIB='AGENT-GENERAL-MIB'
        Object= 'agentSerialNumber' #'1.3.6.1.4.1.17.1.12.1.1.12.0'
        dic_serial=getnext(self.__deviceIP, self.__devicePort, MIB, Object) 
        return(dic_serial)


    
