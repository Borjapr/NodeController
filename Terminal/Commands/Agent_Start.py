from Lib.VTY import _Command

class Command_Agent_Start(_Command):
    def getCommand(self):   return('agent start')

    def getShortHelp(self): return('start all the agents')

    def getLongHelp(self):  return(
            'start all the agents cofigured.\n' +
            'agent start')

    def run(self, *args):
        if(len(args) > 0): return(self.getLongHelp())
        self.getHandler().agent_start()
        return('Start all agents request sent.')


