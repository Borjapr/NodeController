import grpc, logging
from concurrent import futures
from Lib.ParameterChecking import checkType, checkAttr, checkIPv4, checkPort,checkInteger

class Server(object):
    def __init__(self, dispatchers):
        self.__listenIP = None
        self.__listenPort = None
        self.__numWorkers = None
        self.__server = None
        self.__dispatchers = dispatchers

    @staticmethod
    def checkConfiguration(config):
        checkType('config', (dict,), config)
        checkIPv4('listenIP', checkAttr('listenIP', config))
        checkPort('listenPort', checkAttr('listenPort', config))
        checkInteger('numWorkers', checkAttr('numWorkers', config), 1)

    @staticmethod
    def getDefaultConfig():
        return({
            'listenIP': '0.0.0.0',
            'listenPort': 8000,
            'numWorkers': 10,
        })

    def getConfig(self):
        return({
            'listenIP': self.__listenIP,
            'listenPort': self.__listenPort,
            'numWorkers': self.__numWorkers,
        })

    def configure(self, config):
        Server.checkConfiguration(config)
        self.__listenIP = config.get('listenIP')
        self.__listenPort = config.get('listenPort')
        self.__numWorkers = config.get('numWorkers')
    
    def deconfigure(self):
        self.__listenIP = None
        self.__listenPort = None
        self.__numWorkers = None
        self.__server = None

    def start(self):
        self.__server = grpc.server(futures.ThreadPoolExecutor(max_workers=self.__numWorkers))
        for (dispatcher,adder) in self.__dispatchers: adder(dispatcher, self.__server)

        endPoint = '%s:%d' % (self.__listenIP, self.__listenPort)
        self.__listenPort = self.__server.add_insecure_port(endPoint)
        self.__server.start()

        logger = logging.getLogger(__name__)
        logger.info('Server listening on %s:%d' % (self.__listenIP, self.__listenPort))

    def stop(self):
        self.__server.stop(0)
