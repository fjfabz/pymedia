import copy


class MediaFile(object):
    """
    A media file
    """

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
        @return media's filename
        """
        return self._filename

    def getVideoStreams(self):
        """
        Returns a list of VideoStream instances associated to this media file.
        @return media's video streams (as list)
        """
        return self._videoStreams

    def getAudioStreams(self):
        """
        Returns a list of AudioStream instances associated to this media file.
        @return media's audio streams (as list)
        """
        return self._audioStreams

    def getImageStreams(self):
        """
        Returns a list of ImageStream instances associated to this media file.
        @return media's image streams (as list)
        """
        return self._imageStreams

    def getContainerType(self):
        """
        Returns a the container of this media file.
        @return media's container type
        """
        return self._containerType

    def getDescription(self):
        """
        Returns this media's description.
        @return media's description
        """
        return self._description

    def setVideoStreams(self, videoStreams):
        """
        Sets video streams
        @param videoStreams List of streams
        """
        self._videoStreams = videoStreams

    def setAudioStreams(self, audioStreams):
        """
        Sets audio streams
        @param audioStreams List of streams
        """
        self._audioStreams = audioStreams

    def setImageStreams(self, imageStreams):
        """
        Sets image streams
        @param imageStreams List of streams
        """
        self._imageStreams = imageStreams

    def setFileName(self, filename):
        """
        Sets this media's filename.
        @param filename Path to file
        """
        self._filename = filename

    def setContainerType(self, containerType):
        """
        Sets media's container type
        @param containerType New container type
        """
        self._containerType = containerType

    def setDescription(self, description):
        """
        Sets media's description
        @param containerType New description
        """
        self._description = description

    def __deepcopy__(self, memo):
        # print '__deepcopy__(%s)' % str(memo)
        dpmf = MediaFile()
        dpmf.setFileName(copy.deepcopy(self._filename, memo))
        dpmf.setVideoStreams(copy.deepcopy(self._videoStreams, memo))
        dpmf.setAudioStreams(copy.deepcopy(self._audioStreams, memo))
        dpmf.setImageStreams(copy.deepcopy(self._imageStreams, memo))
        dpmf.setContainerType(copy.deepcopy(self._containerType, memo))
        dpmf.setDescription(copy.deepcopy(self._description, memo))
        
        # print 'self  :', self
        # print 'dpmf:', dpmf
        # print 'dpmf is l:', (dpmf is self)
        # print 'dpmf == l:', (dpmf == self)
        
        return dpmf
