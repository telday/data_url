import re
import base64

DATA_URL_RE = re.compile(
    r"data:(?P<MIME>[\w-]+\/[\w+-]+(;[\w-]+\=[\w-]+)?)(?P<encoded>;base64)?,(?P<data>[\w\d.~%\=\/\+-]+)"
)

def construct_data_url(mime_type, base64_encoded, data):
    """
    Helper method for just creating a data URL from some data. If this
    URL will persist it is recommended to create a full DataURL object

    If the data is a string type and the base64_encode flag is set to True then
    this function assumes the data is already base64 encoded and decodes it. Otherwise
    the data is passed through as is.

    Args:
        mime_type (str)
        base64_encoded (boolean): Whether or not the URL data should be base64 encoded. If True the data
            passed to this method is also assumed to be base64 encoded. This parameter is ignored when
            data is bytes type and data is assumed to not be encoded.
        data (str | bytes): The actual url data.

    Returns:
        str: The data URL.
    """
    if type(data) == str:
        data_url = DataURL.from_data(mime_type, base64_encoded, data)
    else:
        data_url = DataURL.from_byte_data(mime_type, data)
    return data_url.url

class DataURL:
    URL_FORMAT = "data:{mime_type}{encoded},{data}"
    ENCODING_STRING = ";base64"

    @classmethod
    def from_url(cls, url):
        """
        Create a new DataURL object from an existing URL. Useful for retrieving
        data from a data URL.

        Args:
            url (str)
        Returns:
            DataURL: A new DataURL object.
        """
        data_url = cls()
        data_url._url = url
        data_url.__parse_url()
        return data_url

    @classmethod
    def from_data(cls, mime_type, base64_encoded, data):
        """Create a new data URL from a mime type and data

        If the data is a string type and the base64_encoded flag is set to True then
        this function assumes the data is already base64 encoded and decodes it. Otherwise
        the data is passed through as is.

        Args:
            mime_type (str)
            base64_encoded (boolean): Whether or not the URL data should be base64 encoded. If True the data
                passed to this method is also assumed to be base64 encoded.
            data (str): The actual url data.
        Returns:
            DataURL: A new DataURL object.
        """
        data_url = cls()
        data_url._mime_type = mime_type
        data_url._is_base64_encoded = base64_encoded

        if type(data) == str and base64_encoded:
            data_url._data = base64.b64decode(data)
        elif type(data) == str:
            data_url._data = data
        else:
            raise TypeError('Data must be a string type')
        return data_url

    @classmethod
    def from_byte_data(cls, mime_type, data):
        """Create a new data URL from a mime type and byte data.

        This method works similarly to from_data, however because the data is bytes type it will
        automatically turn on base64 encoding. It also assumes that the data is not already
        base64 encoded. If you have base64 encoded bytes convert them to a string then
        use the `from_data` method.

        Args:
            mime_type (str)
            data (bytes): The actual url data.
        Returns:
            DataURL: A new DataURL object.
        """
        if type(data) != bytes:
            raise TypeError('Data must be a bytes type')

        data_url = cls()
        data_url._mime_type = mime_type
        data_url._is_base64_encoded = True
        data_url._data = data

        return data_url

    def __parse_url(self):
        """Parses a data URL to get each individual element and sets the
        respecting class attributes."""
        match = DATA_URL_RE.fullmatch(self._url)
        self._is_base64_encoded = match.group('encoded') is not None
        self._mime_type = match.group("MIME")
        raw_data = match.group('data')
        if self._is_base64_encoded:
            self._data = base64.b64decode(raw_data)
        else:
            self._data = raw_data

    def __construct_url(self):
        """Constructs an actual data URL string from class attributes."""
        return self.URL_FORMAT.format(
            mime_type=self._mime_type,
            encoded=self.ENCODING_STRING if self._is_base64_encoded else "",
            data=self.encoded_data
        )

    def __str__(self):
        return self.url

    @property
    def url(self):
        if not hasattr(self, '_url'):
            self._url = self.__construct_url()
        return self._url

    @property
    def is_base64_encoded(self):
        """Whether or not the data URL data is base64 encoded"""
        return self._is_base64_encoded

    @property
    def mime_type(self):
        return self._mime_type

    @property
    def data(self):
        """The raw data of the URL"""
        return self._data

    @property
    def encoded_data(self):
        """The encoded data of the URL"""
        if self._is_base64_encoded:
            return base64.b64encode(self._data).decode('utf-8')
        return self._data
