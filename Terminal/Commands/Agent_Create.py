from Lib.VTY import _Command

class Command_Agent_Create(_Command):
    def getCommand(self):   return('agent create')

    def getShortHelp(self): return('Create agent rmon or snmp')

    def getLongHelp(self):  return(
            'Create agent rmon or snmp, necessary: (nameagent,typeagent (rmon or snmp),ip,port,mpModel).\n' +
            '    agent create')

    def run(self, *args):
        if(len(args) < 5 ): return(self.getLongHelp())
        argumentos = list(args)
        ok = self.getHandler().agent_create(argumentos[0],argumentos[1],argumentos[2],argumentos[3],argumentos[4])
        return(ok)

