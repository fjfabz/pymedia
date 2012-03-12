from stream.mediastream import MediaStream


class VideoStream(MediaStream):
    """
    A video stream
    """

    def __init__(self, filename=None, codecLongName=None, codecTag=None,
                 codecTagString=None, codecName=None, streamIndex=None,
                 framerateMin=None, width=None, height=None, quality=None):
        """
        Constructor
        @param: filename Path to media file
        @param: codecLongName Codec long name
        @param: codecTag Codec id/tag
        @param: codecTag Codec Tag string
        @param: codecName Codec name
        @param: streamIndex Stream Index in media
        @param: framerateMin Minimum framerate
        @param: width Video width
        @param: Hieght Video height
        @param: quality Video quality
        """
        super(VideoStream, self).__init__(filename, "video", codecLongName,
                                          codecTag, codecTagString, codecName,
                                          streamIndex)
        self._framerateMin = framerateMin
        self._width = int(width) if (width != None) else None
        self._height = int(height) if (height != None) else None
        self._quality = quality

    def getWidth(self):
        """
        Returns this media's width
        @return media's width
        """
        return self._width

    def getHeight(self):
        """
        Returns this media's height
        @return media's height
        """
        return self._height

    def getFramerateMin(self):
        """
        Returns this media's framerate
        @return media's framerate
        """
        return self._framerateMin

    def getQuality(self):
        """
        Returns this media's quality
        @return media's quality
        """
        return self._quality
