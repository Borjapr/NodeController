import argparse, logging, threading, signal, sys
from Lib._Configuration import _Configuration
from Lib.LoggerConfigurator import LoggerConfigurator
from Lib.ParameterChecking import checkType, checkAttr
from Manager import Manager

from Protocol.IPFIX.Session import Session
from Protocol.IPFIX.Exporter import Exporter
from Protocol.IPFIX.TemplatesCatalog import TemplatesCatalog

class Configuration(_Configuration):
    def _validate(self):
        config = checkType('config', (dict,), self.data)
        LoggerConfigurator.checkConfiguration(checkAttr('logger', config))
        Manager.checkConfiguration(checkAttr('manager', config))

manager = None
terminate = threading.Event()
terminate.daemon = True
ipfixExporter = None

def stop():
    global manager, terminate,ipfixExporter
    if((manager is not None) and (manager.isRunning())): manager.stop()
    terminate.set()
    
    if((ipfixExporter is not None) and (ipfixExporter.isRunning())):
    	ipfixExporter.stop()
    

def signalHandler(signal, frame):
    logger = logging.getLogger(__name__)
    logger.info('[signalHandler] You pressed Ctrl+C!')
    stop()

def main():
    global manager, terminate,ipfixExporter
    signal.signal(signal.SIGINT, signalHandler)
    signal.signal(signal.SIGTERM, signalHandler)

    loggerConfig = None
    try:
        terminate.clear()
        parser = argparse.ArgumentParser(description='IE Agent')
        parser.add_argument('config', metavar='config', type=argparse.FileType('r'), help='configuration file')
        args = parser.parse_args()
        config = Configuration.createFromFile(args.config).get()
        

        loggerConfig = LoggerConfigurator()
        loggerConfig.configure(config['logger'])

        
        #Configure Templates Catalog
        templatesCatalog = TemplatesCatalog()
        templatesCatalog.configure(config['templatesCatalog'])

        #Configure IPFIX exporter
        obsDomainId = 0
        ipfixSession = Session()
        ipfixSession.getDomain(obsDomainId)
        ipfixExporter = Exporter(ipfixSession)
        ipfixExporter.configure(config['ipfixExporter'])
        ipfixExporter.start()
        templatesCatalog.injectAllTemplates(ipfixExporter)

        #Configure manager
        manager = Manager(terminate,ipfixExporter,templatesCatalog)
        manager.configure(config['manager'])
        manager.start()


        # Ctrl + C tears down modules and sets terminate event
        while(not terminate.wait(0.1)): pass

        if(manager is not None):
            if(manager.isRunning()): manager.stop()
            manager.deconfigure()

        loggerConfig.deconfigure()
        loggerConfig = None

        return(0)
    except Exception as e:
        stop()
        if(loggerConfig is None):
            print 'Exception:', e
        else:
            logger = logging.getLogger(__name__)
            logger.error(str(e))
            logger.exception(e)
        return(1)

if(__name__ == '__main__'):
    sys.exit(main())
