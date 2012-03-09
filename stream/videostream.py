from stream.mediastream import MediaStream

class VideoStream(MediaStream):
	"""
        A video media
        """
	def __init__(self,filename=None,codecLongName=None,codecTag=None, codecTagString=None, codecName=None, streamIndex=None,framerateMin=None, width=None, height=None, quality=None):
		"""
            Constructor
            @param: file Path to media file
            @param: codecLongName Codec long name
            @param: codecTag Codec id/tag
            @param: streamIndex Stream Index in media
            @param: framerateMin Minimum framerate
            """
		super(VideoStream, self).__init__(filename, "video",codecLongName, codecTag, codecTagString, codecName, streamIndex)
		self._framerateMin = framerateMin
		self._width = int(width) if (width != None) else None
		self._height = int(height) if (height != None) else None
		self._quality = quality
    
	def getWidth(self):
		"""
            Returns this media's width
            """
		return self._width
    
	def getHeight(self):
		"""
            Returns this media's height
            """
		return self._height
    
	def getFramerateMin(self):
		"""
            Returns this media's framerate
            """
		return self._framerateMin
    
	def getQuality(self):
		"""
            Returns this media's width
            """
		return self._quality
