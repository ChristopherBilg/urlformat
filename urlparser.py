#!/usr/bin/env python3
"""
Parser class for parsing through web urls.
"""


import re


class UrlParser(object):
    """
    Main url parser class.
    """
    def __init__(self, url):
        """
        Initialization method.
        The url parameter must be a valid url of http or https
        """
        self.match = re.search(
            r"^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?",
            url)
        return

    def get_url(self):
        """
        Getter method for the url itself.
        """
        return self.match.group(0)

    def set_url(self, url):
        """
        Setter method for the url itself.
        """
        self.match = re.search(
            r"^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?",
            url)
        return

    def get_scheme(self):
        """
        Getter method for the url scheme. Ex: http, https, skype
        """
        return self.match.group(2)

    def get_authority(self):
        """
        Getter method for the authority (domain) of the url.
        """
        return self.match.group(4)

    def get_path(self):
        """
        Getter method for the path that the url contains.
        """
        return self.match.group(5)

    def get_query(self):
        """
        Getter method for the [optional] query contained in the url.
        Ex: ?test=example
        """
        return self.match.group(7)

    def get_fragment(self):
        """
        Getter method for the [optional] fragment contained in the url.
        Ex: #example
        """
        return self.match.group(9)


if __name__ == "__main__":
    GOOGLE = "https://www.google.com/test#products"
    REDDIT = "https://reddit.com?name=Glumpz"
    RANDOM = "http://[1000::1001:1510]/web/page?userId=0123456789#fragment"

    print UrlParser(GOOGLE).get_scheme()
    print UrlParser(REDDIT).get_scheme()
    print UrlParser(RANDOM).get_scheme()
    print UrlParser(GOOGLE).get_authority()
    print UrlParser(REDDIT).get_authority()
    print UrlParser(RANDOM).get_authority()
    print UrlParser(GOOGLE).get_path()
    print UrlParser(REDDIT).get_path()
    print UrlParser(RANDOM).get_path()
    print UrlParser(GOOGLE).get_query()
    print UrlParser(REDDIT).get_query()
    print UrlParser(RANDOM).get_query()
    print UrlParser(GOOGLE).get_fragment()
    print UrlParser(REDDIT).get_fragment()
    print UrlParser(RANDOM).get_fragment()
