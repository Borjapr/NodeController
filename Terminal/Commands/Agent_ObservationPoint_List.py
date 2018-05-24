from Lib.VTY import _Command

class Command_Agent_ObservationPoint_List(_Command):
    def getCommand(self):   return('agent observationpoint list')

    def getShortHelp(self): return('Show all de op configured')

    def getLongHelp(self):  return(
            'Show all de op (Observation Point) configured from all agents .\n' +
            'agent observationpoint list')

    def run(self, *args):

        if(len(args) > 0): return(self.getLongHelp())
        observationpoints = self.getHandler().agent_getops()
        stringtotal = "\n \n"
        for value in observationpoints.ops:
            #print str(value.observationPointId)
            #print str(value.agent)
            #print str(value.componentId)
            #print str(value.componentType)
            #print str(value.templateId)
            #print str(value.monitoringPeriod)
            string = " ObservationDomain: %s \n ObservationPoint: %s \n  Enable: %s \n  Agent: %s \n  ComponentId: %s \n  ComponentType: %s \n  templateId: %s \n  monitoringPeriod: %s \n ------------------------ \n" \
            % (str(value.observationDomainId),str(value.observationPointId),str(value.enable),str(value.agent),str(value.componentId),\
                str(value.componentType),str(value.templateId),str(value.monitoringPeriod))
            stringtotal = stringtotal + string

        return('Observation Points: %s' % str(stringtotal))
