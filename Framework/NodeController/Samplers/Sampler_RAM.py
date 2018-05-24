from ._Sampler import _Sampler
from .sample import Sample
from nodecontroller.GetBulkRAM import getbulkram
from collections import defaultdict
from datetime import datetime

class Sampler_RAM(_Sampler):

    CALLBACK_MESSAGE_RAM = 'receivedMessageRAM'

    templateId = 502

    OPTION_TOTAL = 'TOTAL'
    OPTION_USED = 'USED'
    OPTION_UTILIZATION = 'UTILIZATION'
    OPTIONS = [
        OPTION_TOTAL,
        OPTION_USED,
        OPTION_UTILIZATION
    ]

    def __init__(self,objetsnmp):
        _Sampler.__init__(self)
        self.__dics_RAM=defaultdict(dict)
        self._objetsnmp=objetsnmp
        self._log = objetsnmp._log
        self._mpModel = objetsnmp._mpModel
        self._log.debug("INIT in Sampler_RAM")

    def validate(self):
        self._log.debug("check in the RAM Sampler if the templateid matches the one that has been passed")
        if(self._templateId != Sampler_RAM.templateId):
            self._log.error("Incorrect templateId should be 502")
        return(None)

    def do_sampling (self):
        self._log.debug("do_sampling in Sampler_RAM")
        
        dic_RAM= getbulkram(self._objetsnmp.getDeviceIP(), self._objetsnmp.getDevicePort())
        

        delta = datetime.utcnow() - datetime(1970, 1, 1)
      
        valueslist =  []
        try:
            values={'observationPointId': self._observationpoint,
                'agentDRAMutilizationTotalDRAM': dic_RAM['agentDRAMutilizationTotalDRAM'][1],
                'agentDRAMutilizationUsedDRAM': dic_RAM['agentDRAMutilizationUsedDRAM'][1],
                'agentDRAMutilization':  dic_RAM['agentDRAMutilization'][1]}
        except:
            values={'observationPointId': self._observationpoint,
                'agentDRAMutilizationTotalDRAM': 0,
                'agentDRAMutilizationUsedDRAM': 0,
                'agentDRAMutilization':  0
            }
        valueslist.append(values)

        sample = Sample()
        sample.setObsDomainId(self._observationdomain)
        sample.setTimeStamp(delta.total_seconds())
        sample.setTemplateId(Sampler_RAM.templateId)
        sample.setData(valueslist) 
            
        
        self._log.debug("runcallbacks in ram sampler")

        self._objetsnmp._runCallbacks(Sampler_RAM.CALLBACK_MESSAGE_RAM,sample)
        self._scheduleNext()

            
           
    def get_sampling (self):
        return(self.__dics_RAM)
