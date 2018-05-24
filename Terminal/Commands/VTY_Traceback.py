from Lib.VTY import _Command

class Command_VTY_Traceback(_Command):
    def getCommand(self):   return('vty traceback')

    def getShortHelp(self): return('Manage exception traceback dump behavior.')

    def getLongHelp(self):  return(
            'Manage exception traceback dump behavior.\n' +
            '    vty traceback state  get exception traceback dump state\n' +
            '    vty traceback full   enable exception traceback dump\n' +
            '    vty traceback none   disable exception traceback dump')

    def run(self, *args):
        if(len(args) != 1): return('Invalid arguments.\n' + self.getLongHelp())
        
        vty = self.getVTY()

        if(args[0] == 'full'):
            vty.setDumpTraceback(True)
        elif(args[0] == 'none'):
            vty.setDumpTraceback(False)

        if(args[0] in ('state', 'full', 'none')):
            return('Exception Traceback Dump: %s' % (
                'full' if(vty.getDumpTraceback()) else 'none'))
        return('Invalid arguments.\n' + self.getLongHelp())
