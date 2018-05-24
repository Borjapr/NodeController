from ._Sampler import _Sampler
from collections import defaultdict
from .sample import Sample
from nodecontroller.GetBulkIftable import getbulkiftable
from datetime import datetime

class Sampler_ifTable(_Sampler):
    CALLBACK_MESSAGE_ifTable = 'receivedMessageifTable'
    templateId = 505
    def __init__(self,objetsnmp):
        _Sampler.__init__(self)
        self.__dics_ifTable=defaultdict(dict)
        self._objetsnmp=objetsnmp
        self._log = objetsnmp._log
        self._mpModel = objetsnmp._mpModel
        self._log.debug("INIT iftable sampler")

    def validate(self):
        self._log.debug("check in the iftable Sampler if the templateid matches the one that has been passed")
        if (self._templateId != Sampler_ifTable.templateId):
            return("TemplateId incorrecto deberia ser 505")


    def do_sampling (self):
        self._log.debug("Estas en do_sampling de Sampler_ifTable")
        #Diccionario que contiene la tabla ifTable
        dic_ifTable = getbulkiftable(self._objetsnmp.getDeviceIP(), self._objetsnmp.getDevicePort())
       


        delta = datetime.utcnow() - datetime(1970, 1, 1)
        valueslist =  []

        for key,value in dic_ifTable['ifIndex'].iteritems():

            values={'observationPointId': self._observationpoint,
                    'ifIndex': dic_ifTable['ifIndex'][key],
                    'ifDescr': dic_ifTable['ifDescr'][key],
                    'ifType' : dic_ifTable['ifType'][key],
                    'ifSpeed' : dic_ifTable['ifSpeed'][key],
                    'ifPhysAddress': dic_ifTable['ifPhysAddress'][key],
                    'ifAdminStatus': dic_ifTable['ifAdminStatus'][key],
                    'ifOperStatus' : dic_ifTable['ifOperStatus'][key],
                    'ifLastChange' : dic_ifTable['ifLastChange'][key],
                    'ifInOctets' : dic_ifTable['ifInOctets'][key],
                    'ifInUcastPkts' : dic_ifTable['ifInUcastPkts'][key],
                    'ifInNUcastPkts' : dic_ifTable['ifInNUcastPkts'][key],
                    'ifInDiscards' :dic_ifTable['ifInDiscards'][key],
                    'ifInErrors': dic_ifTable['ifInErrors'][key],
                    'ifInUnknownProtos': dic_ifTable['ifInUnknownProtos'][key],
                    'ifOutOctets' : dic_ifTable['ifOutOctets'][key],
                    'ifOutUcastPkts' : dic_ifTable['ifOutUcastPkts'][key],
                    'ifOutNUcastPkts' : dic_ifTable['ifOutNUcastPkts'][key],
                    'ifOutDiscards' : dic_ifTable['ifOutDiscards'][key],
                    'ifOutErrors' : dic_ifTable['ifOutErrors'][key],
                    'ifOutQLen' : dic_ifTable['ifOutQLen'][key],
                    'ifSpecific' : dic_ifTable['ifSpecific'][key]}
            valueslist.append(values)
        
        sample = Sample()
        sample.setObsDomainId(self._observationdomain)
        sample.setTimeStamp(delta.total_seconds())
        sample.setTemplateId(Sampler_ifTable.templateId)
        sample.setData(valueslist) 
          
        
        #Llamamos a la funcion receiver de Manager cuando hemos almacenado maxbuffer muestras y le pasamos el diccioanrio 
        #que contiene dichas muestras   
                 
        self._objetsnmp._runCallbacks(Sampler_ifTable.CALLBACK_MESSAGE_ifTable,sample)
        self._scheduleNext()
                

    def get_sampling (self):
        return(self.__dics_ifTable)
