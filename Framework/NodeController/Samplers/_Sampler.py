import threading
from Lib._Object import _Object

#example Timer
#def hello():
#    print "hello, world"
#
#t = Timer(30.0, hello)
#t.start() # after 30 seconds, "hello, world" will be printed

class _Sampler(_Object):
    def __init__(self):
        self._terminate = threading.Event()
        self._terminate.daemon = True
        self._timer = None
        self._monitoringPeriod = None
        self._observationdomain = None
        self._observationpoint = None
        self._options = None
        self._log = None
        self._templateId = None

    def validate(self):
        raise Exception("To be Implement")

    def configure(self,monitoringPeriod,observationDomain,observationpoint,templateId,options = None):
        self._log.debug("Configure in sampler") 
        self._monitoringPeriod = monitoringPeriod
        self._observationdomain = observationDomain
        self._observationpoint = observationpoint
        self._templateId = templateId
        self._options = options
        return (self.validate())
        

    def start(self):
        self._log.debug("start in sampler") 
        self._terminate.clear()
        self._scheduleNext()

    def stop(self):
        self._log.debug("stop in sampler") 
        self._terminate.set()
        if (self._timer is not None):
            self._timer.cancel()
            self._timer=None

    def _scheduleNext(self):
        self._log.debug("In  _scheduleNext") 
        if(self._terminate.isSet()):
            return
        self._timer = threading.Timer(self._monitoringPeriod, self.do_sampling)
        self._timer.daemon = True
        self._timer.start()

    def do_sampling (self):
        raise Exception("To be Implement")

