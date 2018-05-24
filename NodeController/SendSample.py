from Protocol.IPFIX.Message import Message as IPFIXMessage
from Protocol.IPFIX.DataRecord import DataRecord as IPFIXDataRecord

def SendSample(ipfixExporter, sample,logger):
    obsDomainId = sample.getObsDomainId()
    templateId = sample.getTemplateId()
    timeStamp = sample.getTimeStamp()
    datas = sample.getData()

    ipfixSession = ipfixExporter.getSession()
    domain = ipfixSession.getDomain(obsDomainId)

    if(not domain.hasExporterTemplate(templateId)):
        logger.warning('Sample Ignored: its does not has template(%s)' % (templateId))

    template = domain.getExporterTemplate(templateId)

    message = IPFIXMessage.create(ipfixSession, obsDomainId, timeStamp)
    dataSet = message.addDataSet(templateId)
    for data in datas:
        dataSet.addRecord(IPFIXDataRecord.create(template,data))
    ipfixExporter.sendMessage(message)