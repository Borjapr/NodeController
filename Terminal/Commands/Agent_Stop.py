from Lib.VTY import _Command

class Command_Agent_Stop(_Command):
    def getCommand(self):   return('agent stop')

    def getShortHelp(self): return('stop all the agents')

    def getLongHelp(self):  return(
            'stop all the agents cofigured.\n' +
            'agent stop')

    def run(self, *args):
        if(len(args) > 0): return(self.getLongHelp())
        self.getHandler().agent_stop()
        return('stop all agents request sent.')


