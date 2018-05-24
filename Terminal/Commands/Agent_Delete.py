from Lib.VTY import _Command

class Command_Agent_Delete(_Command):
    def getCommand(self):   return('agent delete')

    def getShortHelp(self): return('Delete agent rmon or snmp')

    def getLongHelp(self):  return(
            'Delete agent rmon or snmp, necessary: nameagent.\n' +
            '    agent delete')

    def run(self, *args):
        if(len(args) < 1 ): return(self.getLongHelp())
        argumentos = list(args)
        ok = self.getHandler().agent_delete(argumentos[0])
        return(ok)
