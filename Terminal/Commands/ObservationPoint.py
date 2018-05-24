from Lib.VTY import _Command

class Command_ObservationPoint(_Command):
    def getCommand(self):   return('agent observationpoint')

    def getShortHelp(self): return('manage the ops')

    def getLongHelp(self):  return(
            'Manage the observationspoints. To see a list of available subCommands, try with: help manager\n' +
            'agent observationpoint <subCommand> [...]')

    def run(self, *args):
        return(self.getLongHelp())
