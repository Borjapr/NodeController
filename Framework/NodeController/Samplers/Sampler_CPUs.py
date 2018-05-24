from ._Sampler import _Sampler
from .sample import Sample
from nodecontroller.GetBulkCPU import getbulkcpu
from collections import defaultdict
from datetime import datetime
import time
class Sampler_CPUs(_Sampler):
    CALLBACK_MESSAGE_CPUS = 'receivedMessageCPUs'

    templateId = 503

    TIME_5 = 5
    TIME_60 = 60
    TIME_300 = 300

    TIMES = [ 
        TIME_5,
        TIME_60,
        TIME_300 
    ]

    def __init__(self,objetsnmp):
        _Sampler.__init__(self)
        self.__dics_CPUs=defaultdict(dict)
        self._objetsnmp=objetsnmp
        self._log = objetsnmp._log
        self._mpModel = objetsnmp._mpModel
        self._log.debug("Init in CPUs Sampler")

    def validate(self):
        self._log.debug("check in the CPUs Sampler if the templateid matches the one that has been passed")
        if (self._templateId != Sampler_CPUs.templateId):
            return("Incorrect templateId should be 503")

    def do_sampling (self):
        self._log.debug("do_sampling in Sampler_CPUs")

        #Diccionario que contiene la tabla CPUs        
        start_time = time.time()
        dic_CPUs= getbulkcpu(self._objetsnmp.getDeviceIP(), self._objetsnmp.getDevicePort())
    
    
        
        self._log.debug(("--- %s seconds ---" % (time.time() - start_time)))

        #Diccionario que contiene los distintos diccionarios de tabla CPUs
        delta = datetime.utcnow() - datetime(1970, 1, 1)

        valueslist =  []

        try:
            values={'observationPointId': self._observationpoint,
                'agentCPUutilizationIn5sec': dic_CPUs['agentCPUutilizationIn5sec'][0],
                'agentCPUutilizationIn1min': dic_CPUs['agentCPUutilizationIn1min'][0],
                'agentCPUutilizationIn5min': dic_CPUs['agentCPUutilizationIn5min'][0]}
        except:
            values={'observationPointId': self._observationpoint,
                'agentCPUutilizationIn5sec': 0,
                'agentCPUutilizationIn1min': 0,
                'agentCPUutilizationIn5min': 0}


        valueslist.append(values)

        sample = Sample()
        sample.setObsDomainId(self._observationdomain)
        sample.setTimeStamp(delta.total_seconds())
        sample.setTemplateId(Sampler_CPUs.templateId)
        sample.setData(valueslist) 
        
        #Llamamos a la funcion receiver de Manager cuando hemos almacenado maxbuffer muestras y le pasamos el diccioanrio 
        #que contiene dichas muestras
        self._log.debug("runcallbacks in cpus sampler")

        self._objetsnmp._runCallbacks(Sampler_CPUs.CALLBACK_MESSAGE_CPUS,sample)
        self._scheduleNext()

        
       

    def get_sampling (self):
        return(self.__dics_CPUs)
