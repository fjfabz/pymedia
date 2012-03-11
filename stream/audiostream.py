from stream.mediastream import MediaStream


class AudioStream(MediaStream):
    """
    An audio media
    """

    def __init__(self, filename=None, codecLongName=None, codecTag=None,
                 codecTagString=None, codecName=None, streamIndex=None,
                 bitPerSample=None, sampleRate=None):
        """
        Constructor
        @param: file Path to media file
        @param: codecLongName Codec long name
        @param: codecTag Codec id/tag
        @param: streamIndex Stream Index in media
        @param: bitPerSample Bits per sample
        @param: sampleRate Sample rate in Hz
        """
        super(AudioStream, self).__init__(filename, "audio", codecLongName,
                                          codecTag, codecTagString,
                                          codecName, streamIndex)
        self._mediaType = "audio"
        self._bitPerSample = bitPerSample
        self._sampleRate = sampleRate  # in hz
        self._streamIndex = streamIndex

    def getBitPerSample(self):
        """
        Returns this media's bit per sample
        """
        return self._bitPerSample

    def getSampleRate(self):
        """
        Returns this media's sample rate
        """
        return self._sampleRate
