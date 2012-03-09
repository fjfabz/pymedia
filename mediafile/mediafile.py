class MediaFile(object):
	def __init__(self):
		self._filename = None
		self._videoStreams = list()
		self._audioStreams = list()
		self._imageStreams = list()
		self._containerType = None
		self._description = ""
    
	def getFileName(self):
		"""
            Returns this media's filename. 
            """
		return self._filename
    
	def getVideoStreams(self):
		"""
            Returns a list of VideoStream instances associated to this media file. 
            """
		return self._videoStreams
    
	def getAudioStreams(self):
		"""
            Returns a list of AudioStream instances associated to this media file. 
            """
		return self._audioStreams
    
	def getImageStreams(self):
		"""
            Returns a list of ImageStream instances associated to this media file. 
            """
		return self._imageStreams
    
	def getContainerType(self):
		"""
            Returns a the container of this media file.
            """
		return self._containerType
    
	def getDescription(self):
		"""
            Returns this media's description. 
            """
		return self._description
    
	def setVideoStreams(self, videoStreams):
		self._videoStreams = videoStreams
    
	def setAudioStreams(self, audioStreams):
		self._audioStreams = audioStreams
    
	def setImageStreams(self, imageStreams):
		self._imageStreams = imageStreams
    
	def setFileName(self, filename):
		"""
            Sets this media's filename. 
            """
		self._filename = filename
    
	def setContainerType(self, containerType):
		self._containerType = containerType
    
	def setDescription(self, description):
		self._description = description

