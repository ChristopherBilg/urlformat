"""
Error handling classes for URL's.
"""


class URLError(Exception):
    """
    Base error class for URL errors.
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


class SitemapError(Exception):
    """
    Base error class for Sitemap errors.
    """
    pass


class SitemapNotFoundError(SitemapError):
    """
    Raised when a sitemap is not found in a specific robots.txt file.
    """
    pass


class RobotError(Exception):
    """
    Base error class for Robot errors.
    """
    pass


class RobotNotFoundError(RobotError):
    """
    Raised when a robots file is not found at a given location.
    """
    pass
