from ._Sampler import _Sampler
from .sample import Sample
from nodecontroller.GetBulkStatistics import getbulkstatistics
from collections import defaultdict
from datetime import datetime

class Sampler_Statistics(_Sampler):
  CALLBACK_MESSAGE_STATISTICS = 'receivedMessageStatistics'
  templateId = 501
  def __init__(self,objetrmon):
    _Sampler.__init__(self)
    self.__dics_statistics=defaultdict(dict)
    self._objetrom=objetrmon
    self._log = objetrmon._log
    self._mpModel = objetrmon._mpModel
    self._log.debug("init in statistics sampler")

  def validate(self):
    self._log.debug("check in the Statistics Sampler if the templateid matches the one that has been passed")
    if (self._templateId != Sampler_Statistics.templateId):
        return("Incorrect templateId should be 501")
        
  def do_sampling (self):

    self._log.debug("do_sampling in statistics Sampler")

    

    self._log.debug("getbulkstatistics")
    dic_statistics = getbulkstatistics(self._objetrom.getDeviceIP(), self._objetrom.getDevicePort())
    

    delta = datetime.utcnow() - datetime(1970, 1, 1)
    valueslist =  []

    for key,value in dic_statistics['etherStatsOversizePkts'].iteritems():

        values={'observationPointId': self._observationpoint,
                'etherStatsOversizePkts': dic_statistics['etherStatsOversizePkts'][key],
                'etherStatsFragments': dic_statistics['etherStatsFragments'][key],
                'etherStatsJabbers' : dic_statistics['etherStatsJabbers'][key],
                'etherStatsCollisions' : dic_statistics['etherStatsCollisions'][key],
                'etherStatsPkts64Octets': dic_statistics['etherStatsPkts64Octets'][key],
                'etherStatsPkts65to127Octets': dic_statistics['etherStatsPkts65to127Octets'][key],
                'etherStatsPkts128to255Octets' : dic_statistics['etherStatsPkts128to255Octets'][key],
                'etherStatsPkts256to511Octets' : dic_statistics['etherStatsPkts256to511Octets'][key],
                'etherStatsPkts512to1023Octets' : dic_statistics['etherStatsPkts512to1023Octets'][key],
                'etherStatsPkts1024to1518Octets' : dic_statistics['etherStatsPkts1024to1518Octets'][key],
                'etherStatsStatus' : dic_statistics['etherStatsStatus'][key],
                'etherStatsDropEvents' :dic_statistics['etherStatsDropEvents'][key],
                'etherStatsOctets': dic_statistics['etherStatsOctets'][key],
                'etherStatsPkts': dic_statistics['etherStatsPkts'][key],
                'etherStatsBroadcastPkts' : dic_statistics['etherStatsBroadcastPkts'][key],
                'etherStatsMulticastPkts' : dic_statistics['etherStatsMulticastPkts'][key],
                'etherStatsCRCAlignErrors' : dic_statistics['etherStatsCRCAlignErrors'][key],
                'etherStatsUndersizePkts' : dic_statistics['etherStatsUndersizePkts'][key]}
        valueslist.append(values)
    
    sample = Sample()
    sample.setObsDomainId(self._observationdomain)
    sample.setTimeStamp(delta.total_seconds())
    sample.setTemplateId(Sampler_Statistics.templateId)
    sample.setData(valueslist) 
    
    self._log.debug("runcallbacks in statistics sampler")
    self._objetrom._runCallbacks(Sampler_Statistics.CALLBACK_MESSAGE_STATISTICS,sample)
    self._scheduleNext()
     

  def get_sampling (self):
    return(self.__dics_statistics)
    
