"""
Error handling classes for URL's.
"""


class URLError(Exception):
    """
    Base error class for other errors.
    """
    pass


class InvalidURLError(URLError):
    """
    Raised when a check is made against an invalid url.
    """
    pass


class UnbuiltURLError(URLError):
    """
    Raised when a url is attempted to be built but cannot be successfully.
    """
    pass
