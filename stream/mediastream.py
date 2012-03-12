class MediaStream(object):
    """
    A media
    """

    def __init__(self, filename=None, mediaType=None, codecLongName=None,
                 codecTag=None, codecTagString=None, codecName=None,
                 streamIndex=None):
        """
        Constructor
        @param: file Path to media file
        @param: codecLongName Codec long name
        @param: codecTag Codec id/tag
        @param: codecTagString Codec tag string
        @param: codecName Codec name
        @param: streamIndex Stream Index in media
        """
        self._mediaType = mediaType
        self._filename = filename
        self._codecLongName = codecLongName
        self._codecTag = codecTag
        self._codecTagString = codecTagString
        self._codecName = codecName
        self._streamIndex = streamIndex

    def getType(self):
        """
        Returns this media's type
        @return media's type
        """
        return self._mediaType

    def getStreamIndex(self):
        """
        Returns this media's stream index
        @return media's stream index
        """
        return self._streamIndex

    def getCodecLongName(self):
        """
        Returns this media's codec long name
        @return media's codec long name
        """
        return self._codecLongName

    def getCodecTag(self):
        """
        Returns this media's codec tag
        @return media's codec tag
        """
        return self._codecTag

    def getCodecTagString(self):
        """
        Returns this media's codec tag string
        @return media's codec tag string
        """
        return self._codecTagString

    def getCodecName(self):
        """
        Returns this media's codec name
        @return media's codec name
        """
        return self._codecName
