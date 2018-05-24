from Lib._Object import _Object

class _Agent(_Object):
    def __init__(self, name):
        _Object.__init__(self, name)
        # define attributes common to all the agents
        self._deviceIP = None
        self._devicePort = None
        self._mpModel = None #mpModel=1 -> SNMPv1 #mpModel =2 -> SNMPv2

    def getDeviceIP(self):
        return(self._deviceIP)

    def getDevicePort(self):
        return(self._devicePort)

    # define other methods common to all the agents
    def configure(self, config):
        raise Exception("To be Implement")
    def start(self):
        raise Exception("To be Implement")
    def disableop(self, observationPointId):
        raise Exception("To be Implement")
    def enableop(self, observationPointId):
        raise Exception("To be Implement")
    def stop(self):
        raise Exception("To be Implement")
    def deleteop(self, observationPointId):
        raise Exception("To be Implement")
    def configureObservationPoint(self, observationPointId, componentId=None, componentType=None,templateId=None, monitoringPeriod=None):
        raise Exception("To be Implement")

    def getConfiguredObservationPoints(self, observationPointId=None):
        raise Exception("To be Implement")