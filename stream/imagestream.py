from stream.mediastream import MediaStream


class ImageStream(MediaStream):
    """
    An image media
    """

    def __init__(self, filename=None, width=None, height=None,
                 quality=None, densityX=None, densityY=None):
        """
        Constructor
        @param: file Path to media file
        @param: width Image width
        @param: height Image height
        @param: quality Image quality
        """
        super(ImageStream, self).__init__(filename=filename, mediaType="image")
        self._width = int(width) if (width != None) else None
        self._height = int(height) if (height != None) else None
        self._quality = quality
        self._densityX = densityX
        self._densityY = densityY

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

    def getQuality(self):
        """
        Returns this media's width
        """
        return self._quality

    def getDensityX(self):
        """
        Returns this media's density X
        """
        return self._densityX

    def getDensityY(self):
        """
        Returns this media's density Y
        """
        return self._densityY
