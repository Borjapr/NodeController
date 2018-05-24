from Lib.VTY import _Command
from Lib.ParameterChecking import checkIPv4Port, checkPort

class Command_VTY_Connect(_Command):
    def getCommand(self):   return('vty connect')

    def getShortHelp(self): return('Disconnect and reconnect to new server.')

    def getLongHelp(self):  return(
            'Disconnect and reconnect to new server.\n' +
            '    vty connect ip:port')

    def run(self, *args):
        if(len(args) != 1): return('Invalid arguments.\n' + self.getLongHelp())

        strReply = 'Invalid arguments:\n'
        try:
            checkIPv4Port('ip:port', args[0])
            serverIP,serverPort = args[0].split(':')
        except Exception as e:
            strReply += ('  Unable to parse endpoint as "ip:port": %s.\n' % str(e))
            strReply += self.getLongHelp()
            return(strReply)

        serverPort = int(serverPort)
        handler = self.getHandler()
        handler.configure({'serverIP': serverIP, 'serverPort': serverPort})
        version = handler.agent_getVersion()
        return('Reconnected to %s:%d.\nAgent Version: %s' % (serverIP, serverPort, version))
