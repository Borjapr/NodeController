from ._Sampler import _Sampler
from .sample import Sample
from nodecontroller.GetBulkFLASH import getbulkflash
from collections import defaultdict
from datetime import datetime

class Sampler_FLASH(_Sampler):
    CALLBACK_MESSAGE_FLASH = 'receivedMessageFLASH'

    templateId = 504

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
        self.__dics_FLASH=defaultdict(dict)
        self._objetsnmp=objetsnmp
        self._log = objetsnmp._log
        self._mpModel = objetsnmp._mpModel
        self._log.debug("Estas en INIT de Sampler_FLASH")

    def validate(self):
        self._log.debug("check in the Flash Sampler if the templateid matches the one that has been passed")
        if (self._templateId != Sampler_FLASH.templateId):
            return("Incorrect templateId should be 504")

    def do_sampling (self):
        self._log.debug("do_sampling in  Flash Sampler")

        #Diccionario que contiene la tabla flash
        dic_FLASH= getbulkflash(self._objetsnmp.getDeviceIP(), self._objetsnmp.getDevicePort())
           
        #Diccionario que contiene los distintos diccionarios de tabla RAM
        delta = datetime.utcnow() - datetime(1970, 1, 1)
        
        valueslist =  []

        try:
            values={'observationPointId': self._observationpoint,
                    'agentFLASHutilizationTotalFLASH': dic_FLASH['agentFLASHutilizationTotalFLASH'][1],
                    'agentFLASHutilizationUsedFLASH': dic_FLASH['agentFLASHutilizationUsedFLASH'][1],
                    'agentFLASHutilization': dic_FLASH['agentFLASHutilization'][1]}
        except:
            values={'observationPointId': self._observationpoint,
                    'agentFLASHutilizationTotalFLASH': 0,
                    'agentFLASHutilizationUsedFLASH': 0,
                    'agentFLASHutilization': 0}
        
        valueslist.append(values)

        sample = Sample()
        sample.setObsDomainId(self._observationdomain)
        sample.setTimeStamp(delta.total_seconds())
        sample.setTemplateId(Sampler_FLASH.templateId)
        sample.setData(valueslist) 
        
        #Llamamos a la funcion receiver de Manager cuando hemos almacenado maxbuffer muestras y le pasamos el diccioanrio 
        #que contiene dichas muestras
        self._log.debug("runcallbacks in flash sampler")

        self._objetsnmp._runCallbacks(Sampler_FLASH.CALLBACK_MESSAGE_FLASH,sample)
        self._scheduleNext()
        
            

    def get_sampling (self):
        return(self.__dics_FLASH)
