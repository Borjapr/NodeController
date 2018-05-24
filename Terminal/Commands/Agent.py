from Lib.VTY import _Command

class Command_Agent(_Command):
    def getCommand(self):   return('agent')

    def getShortHelp(self): return('Manage the agents.')

    def getLongHelp(self):  return(
            'Manage the agents. To see a list of available subCommands, try with: help agent\n' +
            '    agent <subCommand> [...]')

    def run(self, *args):
        return(self.getLongHelp())
