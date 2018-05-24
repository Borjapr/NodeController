class Sample():
	
	def __init__(self):
		self.__ObsDomainId = None
		self.__TemplateId = None
		self.__timeStamp = None
		self.__data = None

	def getObsDomainId(self): return(self.__ObsDomainId)
	def getTemplateId(self): return(self.__TemplateId)#145: { 'name': 'templateId','type': 'unsigned16'},
	def getTimeStamp(self): return(self.__TimeStamp)#ExporttimeUTC
	def getData(self): return(self.__data)
			

	def setObsDomainId(self, ObsDomainId): self.__ObsDomainId=ObsDomainId
	def setTimeStamp(self, timeStamp): self.__TimeStamp=timeStamp
	def setTemplateId(self, templateId): self.__TemplateId=templateId
	def setData(self,data): self.__data = data