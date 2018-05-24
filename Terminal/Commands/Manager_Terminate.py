from Lib.VTY import _Command

class Command_Manager_Terminate(_Command):
    def getCommand(self):   return('manager terminate')

    def getShortHelp(self): return('Terminate the manager.')

    def getLongHelp(self):  return(
            'Terminate the manager.\n' +
            '    manager terminate')

    def run(self, *args):
        if(len(args) > 0): return(self.getLongHelp())
        self.getHandler().manager_terminate()
        return('Terminate request sent.')
