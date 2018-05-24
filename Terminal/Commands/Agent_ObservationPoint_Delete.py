from Lib.VTY import _Command

class Command_Agent_ObservationPoint_Delete(_Command):
    def getCommand(self):   return('agent observationpoint delete')

    def getShortHelp(self): return('Delete op')

    def getLongHelp(self):  return(
            'Delete op(NameAgent, observation Domain,observation point).\n' +
            'agent observationpoint delete')

    def run(self, *args):
        if(len(args) < 3 ): return(self.getLongHelp())
        argumentos = list(args)
        ok = self.getHandler().agent_deleteop(argumentos[0],argumentos[1],argumentos[2])
        return(ok)
