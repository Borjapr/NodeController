import threading
from Protocol.GRPC.IEACP_pb2_grpc import AgentServicer
from Protocol.GRPC.IEACP_pb2 import MsgNull, MsgVersion, MsgOK,MsgOPs,MsgAgents


class NCServicerImpl(AgentServicer):
    def __init__(self, manager):
        self.__manager = manager

    def GetVersion(self, request, context):
        msgVersion = MsgVersion()
        msgVersion.version = self.__manager.getVersion()
        return(msgVersion)

    def Terminate(self, request, context):
        # primero tengo que responder antes de apagar el manager,
        # por eso lo lanzo en un timer
        t = threading.Timer(1.0, self.__manager.stop)
        t.daemon = True
        t.start()
        return(MsgNull())

    def Start(self, request, context):
        t = threading.Timer(1.0, self.__manager.start)
        t.daemon = True
        t.start()
        return(MsgNull())

    def CreateAgent(self, request, context):
        msgOk = MsgOK()
        msgOk.ok = self.__manager.createagent(request.nameAgent, request.Type, request.IP, request.Port, request.mpModel)   
        return(msgOk)     

    def ModifyAgent(self,request, context):
        msgOk = MsgOK()
        msgOk.ok = self.__manager.modifyagent(request.nameAgent, request.Type, request.IP, request.Port, request.mpModel)   
        return(msgOk)    

    def DeleteAgent(self,request, context):
        msgOk = MsgOK()
        msgOk.ok = self.__manager.deleteagent(request.nameAgent)
        return(msgOk)

    def ListAgent(self,request, context):
        msgAgents = MsgAgents()
        dictagents = self.__manager.listagent()
        for nameagent, rest in dictagents.iteritems(): 
                msgAgents.agents.add(nameAgent = nameagent, Type = rest.getName() ,IP = str(rest._deviceIP),\
                 Port = str(rest._devicePort) ,mpModel = str(rest._mpModel))
        return(msgAgents)

    def CreateOP(self, request, context):
        msgOk = MsgOK()
        ok = self.__manager.createop(request.nameAgent, request.observationDomainId, request.observationPointId, request.componentId,\
            request.componentType, request.templateId, request.monitoringPeriod)
        msgOk.ok = ok
        return(msgOk)

    def ModifyOP(self, request, context):
        msgOk = MsgOK()
        ok = self.__manager.modifyop(request.nameAgent, request.observationDomainId, request.observationPointId, request.componentId,\
            request.componentType, request.templateId, request.monitoringPeriod)
        msgOk.ok = ok
        return(msgOk)    

    def DeleteOP(self, request, context):
        msgOk = MsgOK()
        msgOk.ok = self.__manager.deleteop(request.nameAgent, request.observationDomainId, request.observationPointId)
        return(msgOk)
    def EnableOP(self, request, context):
        msgOk = MsgOK()
        msgOk.ok = self.__manager.enableop(request.nameAgent, request.observationDomainId, request.observationPointId)
        return(msgOk)

    def DisableOP(self, request, context):
        msgOk = MsgOK()
        msgOk.ok = self.__manager.disableop(request.nameAgent, request.observationDomainId, request.observationPointId)
        return(msgOk)


    def OP_List(self, request, context):
        msgGetOP = MsgOPs()
        dictop = self.__manager.listop()
        for nameagent, paramop in dictop.iteritems():
            for key,restparam in paramop.iteritems():
                msgGetOP.ops.add(agent = nameagent, observationDomainId = key[0],observationPointId = key[1], componentId = restparam["componentId"],\
                componentType = str(restparam["componentType"]),templateId = restparam["templateId"],\
                monitoringPeriod = restparam["monitoringPeriod"], enable = restparam["enable"])
        return(msgGetOP)

    def StartAgents(self, request, context):
        t = threading.Timer(1.0, self.__manager.startagents)
        t.daemon = True
        t.start()
        return(MsgNull())

    def StopAgents(self, request, context):
        t = threading.Timer(1.0, self.__manager.stopagents)
        t.daemon = True
        t.start()
        return(MsgNull())
