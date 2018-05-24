from Lib.VTY import _Command

class Command_Agent_Modify(_Command):
    def getCommand(self):   return('agent modify')

    def getShortHelp(self): return('Modify agent rmon or snmp')

    def getLongHelp(self):  return(
            'Modify agent rmon or snmp, necessary: (nameagent,typeagent (rmon or snmp),ip,port,mpModel).\n' +
            '    agent modify')

    def run(self, *args):
        if(len(args) < 5 ): return(self.getLongHelp())
        argumentos = list(args)
        ok =self.getHandler().agent_modify(argumentos[0],argumentos[1],argumentos[2],argumentos[3],argumentos[4])
        return(ok)
