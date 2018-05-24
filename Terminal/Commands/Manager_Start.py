from Lib.VTY import _Command

class Command_Manager_Start(_Command):
    def getCommand(self):   return('manager start')

    def getShortHelp(self): return('Start the Manager.')

    def getLongHelp(self):  return(
            'Start the Manager.\n' +
            '    manager start')

    def run(self, *args):
        if(len(args) > 0): return(self.getLongHelp())
        self.getHandler().manager_start()
        return('Start request sent.')

