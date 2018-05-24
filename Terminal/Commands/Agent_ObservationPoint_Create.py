from Lib.VTY import _Command

class Command_Agent_ObservationPoint_Create(_Command):
    def getCommand(self):   return('agent observationpoint create')

    def getShortHelp(self): return('Create op(observation point)')

    def getLongHelp(self):  return(
            'using agent RMON or SNMP,\
            necessary:(nameagent,observationDomain,observationPoint,componentId,componentType,templateId,monitoringPeriod).\n' +
            'agent observationpoint create')

    def run(self, *args):
        if(len(args) < 7 ): return(self.getLongHelp())
        argumentos = list(args)
        ok = self.getHandler().agent_createop(argumentos[0],argumentos[1],argumentos[2],argumentos[3],argumentos[4],argumentos[5],argumentos[6])
        return(ok)

