from Lib.VTY import _Command

class Command_Agent_List(_Command):
    def getCommand(self):   return('agent list')

    def getShortHelp(self): return('List of all agents')

    def getLongHelp(self):  return(
            'List of all agents.\n' +
            '    agent list')

    def run(self, *args):
        if(len(args) > 0): return(self.getLongHelp())
        dictagents = self.getHandler().agent_list()
        stringtotal = "\n"
        for value in dictagents.agents:
            string = "  NameAgent: %s \n  Type: %s \n  IP: %s \n  Port: %s \n  mpModel: %s \n ------------------------ \n" \
            % (str(value.nameAgent),str(value.Type),str(value.IP),str(value.Port),str(value.mpModel))
            stringtotal = stringtotal + string

        return('Agents: %s' % str(stringtotal))     
