from .Sampler_Statistics import Sampler_Statistics
from .Sampler_History import Sampler_History
from .Sampler_ifTable import Sampler_ifTable
from .Sampler_CPUs import Sampler_CPUs
from .Sampler_RAM import Sampler_RAM
from .Sampler_FLASH import Sampler_FLASH

class SamplerFactory(object):
    CLASS_MAPPING = {
        'statistics': Sampler_Statistics,
        'history': Sampler_History,
        'iftable': Sampler_ifTable,
        'CPU': Sampler_CPUs,
        'RAM': Sampler_RAM,
        'FLASH': Sampler_FLASH
    }
    
    @staticmethod
    def get(tipo,agent):
        agent._log.debug("Estamos en sampler factory")
        samplerClass = SamplerFactory.CLASS_MAPPING.get(tipo)
        if(samplerClass is None): raise Exception('Unsupported Sampler: %s' % tipo)
        agent._log.debug("retornamos sample desde sampler factory")
        return(samplerClass(agent))
