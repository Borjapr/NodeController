import grpc
from Lib.ParameterChecking import checkType, checkAttr, checkIPv4, checkPort
from Protocol.GRPC.IEACP_pb2_grpc import AgentStub
from Protocol.GRPC.IEACP_pb2 import MsgNull,MsgCreateAgent,MsgCreateOP,MsgNameAgentOP,MsgNameAgent

class Client(object):
    def __init__(self):
        self.__serverIP = None
        self.__serverPort = None
        self.__channel = None
        self.__agentStub = None

    @staticmethod
    def checkConfiguration(config):
        #Comprobamos configuracion 
        checkType('config', (dict,), config)
        checkIPv4('serverIP', checkAttr('serverIP', config))
        checkPort('serverPort', checkAttr('serverPort', config))

    def configure(self, config):
        #Recibe la configuracin del Main en Terminal
        Client.checkConfiguration(config)
        self.__serverIP = config.get('serverIP')
        self.__serverPort = config.get('serverPort')
        self.__channel = grpc.insecure_channel('%s:%d' % (self.__serverIP, self.__serverPort))
        self.__agentStub = AgentStub(self.__channel)

    def manager_getVersion(self):
        msgNull = MsgNull() #Obtenemos un MsgNull
        msgVersion = self.__agentStub.GetVersion(msgNull) #Utilizando agentestub llamamos a GetVersion  agente pasandole MsgNull
        return(msgVersion.version)

    def manager_terminate(self):
        msgNull = MsgNull()
        _ = self.__agentStub.Terminate(msgNull) #Llamamos a la funcion Terminate de Agente 
        return(None)
    def manager_start(self):
        msgNull = MsgNull()
        _ = self.__agentStub.Start(msgNull)
        return(None)

    def agent_create(self,nameagent,Type,ip,port,mpModel):
        msgCreateAgent = MsgCreateAgent()
        msgCreateAgent.nameAgent = nameagent
        msgCreateAgent.Type = Type
        msgCreateAgent.IP = ip
        msgCreateAgent.Port = port 
        msgCreateAgent.mpModel = mpModel
        ok = self.__agentStub.CreateAgent(msgCreateAgent)
        return(ok.ok)
    def agent_modify(self,nameagent,Type,ip,port,mpModel):
        msgCreateAgent = MsgCreateAgent()
        msgCreateAgent.nameAgent = nameagent
        msgCreateAgent.Type = Type
        msgCreateAgent.IP = ip
        msgCreateAgent.Port = port 
        msgCreateAgent.mpModel = mpModel
        ok = self.__agentStub.ModifyAgent(msgCreateAgent)
        return(ok.ok)

    def agent_delete(self, nameAgent):
        msgNameAgent = MsgNameAgent()
        msgNameAgent.nameAgent = nameAgent
        ok = self.__agentStub.DeleteAgent(msgNameAgent)
        return(ok.ok)

    def agent_list(self):
        msgNull = MsgNull()
        msgAgents = self.__agentStub.ListAgent(msgNull)
        return(msgAgents)

    def agent_createop(self,nameAgent,observationDomainId,observationPointId,componentId,componentType,templateId,monitoringPeriod):
        msgCreateOP = MsgCreateOP()
        msgCreateOP.nameAgent = nameAgent
        msgCreateOP.observationDomainId = int(observationDomainId)
        msgCreateOP.observationPointId = int(observationPointId)
        msgCreateOP.componentType = componentType
        msgCreateOP.componentId = int(componentId)
        msgCreateOP.templateId = int(templateId)
        msgCreateOP.monitoringPeriod = int(monitoringPeriod)
        ok = self.__agentStub.CreateOP(msgCreateOP)
        return(ok.ok)

    def agent_modifyop(self,nameAgent,observationDomainId,observationPointId,componentId,componentType,templateId,monitoringPeriod):
        msgCreateOP = MsgCreateOP()
        msgCreateOP.nameAgent = nameAgent
        msgCreateOP.observationDomainId = int(observationDomainId)
        msgCreateOP.observationPointId = observationPointId
        msgCreateOP.componentType = componentType
        msgCreateOP.componentId = componentId
        msgCreateOP.templateId = templateId
        msgCreateOP.monitoringPeriod = monitoringPeriod
        ok = self.__agentStub.ModifyOP(msgCreateOP)
        return(ok.ok)

    def agent_deleteop(self,nameAgent,observationDomainId,observationPointId):
        msgdeleteOP = MsgNameAgentOP()
        msgdeleteOP.nameAgent = nameAgent
        msgdeleteOP.observationDomainId = int(observationDomainId)
        msgdeleteOP.observationPointId = int(observationPointId)
        ok = self.__agentStub.DeleteOP(msgdeleteOP)
        return(ok.ok)
    def agent_enableop(self,nameAgent,observationDomainId,observationPointId):
        msgenableop = MsgNameAgentOP()
        msgenableop.nameAgent = nameAgent
        msgenableop.observationDomainId = int(observationDomainId)
        msgenableop.observationPointId = int(observationPointId)
        ok = self.__agentStub.EnableOP(msgenableop)
        return(ok.ok)

    def agent_disableop(self,nameAgent,observationDomainId,observationPointId):
        msgdisableop = MsgNameAgentOP()
        msgdisableop.nameAgent = nameAgent
        msgdisableop.observationDomainId = int(observationDomainId)
        msgdisableop.observationPointId = int(observationPointId)
        ok = self.__agentStub.DisableOP(msgdisableop)
        return(ok.ok)


    def agent_getops(self):
        msgNull = MsgNull()
        msgGetOp = self.__agentStub.OP_List(msgNull)
        return(msgGetOp)
        
    def agent_start(self):
        msgNull = MsgNull()
        _ = self.__agentStub.StartAgents(msgNull)
        return(None)

    def agent_stop(self):
        msgNull = MsgNull()
        _ = self.__agentStub.StopAgents(msgNull)
        return(None)