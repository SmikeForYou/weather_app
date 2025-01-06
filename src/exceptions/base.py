

class OriginException(Exception):
    """Base class for all exceptions in this package."""
    pass


class WeatherProviderException(OriginException):
    """Raised when an error occurs in the weather provider."""
    pass

class OriginClientException(OriginException):
    """Raised when an error occurs in the origin server client."""
    pass