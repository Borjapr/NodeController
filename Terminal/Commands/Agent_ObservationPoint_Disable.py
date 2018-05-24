from Lib.VTY import _Command

class Command_Agent_ObservationPoint_Disable(_Command):
    def getCommand(self):   return('agent observationpoint disable')

    def getShortHelp(self): return('Disable sampler in op')

    def getLongHelp(self):  return(
            'Enable sampler in op(NameAgent, observation Domain,observation point).\n' +
            'agent observationpoint enable')

    def run(self, *args):
        if(len(args) < 3 ): return(self.getLongHelp())
        argumentos = list(args)
        ok = self.getHandler().agent_disableop(argumentos[0],argumentos[1],argumentos[2])
        return(ok)
