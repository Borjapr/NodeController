from Lib.VTY import _Command

class Command_Manager_Version(_Command):
    def getCommand(self):   return('manager version')

    def getShortHelp(self): return('Get manager\'s version.')

    def getLongHelp(self):  return(
            'Get manager\'s version.\n' +
            '    manager version')

    def run(self, *args):
        if(len(args) > 0): return(self.getLongHelp())
        version = self.getHandler().manager_getVersion()
        return('manager Version: %s' % str(version))
