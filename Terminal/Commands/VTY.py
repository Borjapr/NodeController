from Lib.VTY import _Command

class Command_VTY(_Command):
    def getCommand(self):   return('vty')

    def getShortHelp(self): return('Manage the VTY.')

    def getLongHelp(self):  return(
            'Manage the VTY. To see a list of available subCommands, try with: help vty\n' +
            '    vty <subCommand> [...]')

    def run(self, *args):
        return(self.getLongHelp())
