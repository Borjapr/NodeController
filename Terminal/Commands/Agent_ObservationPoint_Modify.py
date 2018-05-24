from Lib.VTY import _Command

class Command_Agent_ObservationPoint_Modify(_Command):
    def getCommand(self):   return('agent observationpoint modify')

    def getShortHelp(self): return('Modify op(observation point)')

    def getLongHelp(self):  return(
            'using agent RMON or SNMP,\n\
            necessary:(nameagent,observationDomain,observationPoint,componentId,componentType,templateId,monitoringPeriod).\n' +
            'agent observationpoint modify')

    def run(self, *args):
        if(len(args) < 7 ): return(self.getLongHelp())
        argumentos = list(args)
        ok = self.getHandler().agent_modifyop(argumentos[0],int(argumentos[1]),int(argumentos[2]),int(argumentos[3]),argumentos[4],int(argumentos[5]),int(argumentos[6]))
        return(ok)

