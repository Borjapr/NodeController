from Lib.VTY import _Command

class Command_Manager(_Command):
    def getCommand(self):   return('manager')

    def getShortHelp(self): return('Manage the Manager.')

    def getLongHelp(self):  return(
            'Manage the Manager. To see a list of available subCommands, try with: help manager\n' +
            '    manager <subCommand> [...]')

    def run(self, *args):
        return(self.getLongHelp())
