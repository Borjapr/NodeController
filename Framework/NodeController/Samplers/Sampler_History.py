from ._Sampler import _Sampler
from nodecontroller.GetNext import getnext
from nodecontroller.Set import setnext
from collections import defaultdict
from datetime import datetime


class Sampler_History(_Sampler):
    CALLBACK_MESSAGE_HISTORY = 'receivedMessageHistory'

    def __init__(self,objetrmon):
        _Sampler.__init__(self)
        self.__dics_history=defaultdict(dict)
        self._objetrom=objetrmon
        self._log = objetrom._log
        self._log.debug("Estas en el INIT de Sampler_History")

    def do_sampling (self):
        print "Estas en do_sampling de Sampler_History"
        
        if (self._i == 0):
                #Aqui tenemos un problema debe ser que el router no nos deja hacer set
            self._log.debug("Hacemos set en Sampler_History")
            setnext(self._objetrom.getDeviceIP(), self._objetrom.getDevicePort(),'RMON-MIB','historyControlInterval', self._monitoringPeriod)

        self._log.debug("GetNext en Sampler_History")
        #Diccionario que contiene la tabla history
        dic_history = getnext(self._objetrom.getDeviceIP(), self._objetrom.getDevicePort(),'RMON-MIB','etherHistoryTable')

        #Diccionario que contiene los distintos diccionarios de tabla statistics
        delta = datetime.utcnow() - datetime(1970, 1, 1)
        self.__dics_history[self._i]['timestamp'] = delta.total_seconds()
        self.__dics_history[self._i] = dic_history
            
        #Llamamos a la funcion receiver de Manager cuando hemos almacenado maxbuffer muestras y le pasamos el diccioanrio 
        #que contiene dichas muestras
        
        if(self._i==self._maxbuffer):
            self._runCallbacks(Sampler_History.CALLBACK_MESSAGE_History,self.__dics_history)
            self._i=0
        else:
            self._i=self.i + 1
            self._scheduleNext()
            

    def get_sampling (self):
        return(self.__dics_history)
        
