from Lib.VTY import _Command

class Command_Agent_ObservationPoint_Enable(_Command):
    def getCommand(self):   return('agent observationpoint enable')

    def getShortHelp(self): return('Enable sampler in op')

    def getLongHelp(self):  return(
            'Enable sampler in op(NameAgent, observation Domain,observation point).\n' +
            'agent observationpoint enable')

    def run(self, *args):
        if(len(args) < 3 ): return(self.getLongHelp())
        argumentos = list(args)
        ok = self.getHandler().agent_enableop(argumentos[0],argumentos[1],argumentos[2])
        return(ok)
