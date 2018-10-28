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
        return self.match.group(0) if self.match.group(0) is not None else ""

    def get_scheme(self):
        """
        Getter method for the url scheme. Ex: http, https, skype
        """
        return self.match.group(2) if self.match.group(2) is not None else ""

    def get_authority(self):
        """
        Getter method for the authority (domain) of the url.
        """
        return self.match.group(4) if self.match.group(4) is not None else ""

    def get_path(self):
        """
        Getter method for the path that the url contains.
        """
        return self.match.group(5) if self.match.group(5) is not None else ""

    def get_query(self):
        """
        Getter method for the [optional] query contained in the url.
        Ex: ?test=example
        """
        return self.match.group(7) if self.match.group(7) is not None else ""

    def get_fragment(self):
        """
        Getter method for the [optional] fragment contained in the url.
        Ex: #example
        """
        return self.match.group(9) if self.match.group(9) is not None else ""


class UrlBuilder(object):
    """
    Class to build valid url strings given elementary parts.
    """
    def __init__(self, url=""):
        """
        Initialization method.
        Optional url parameter can be passed. MUST BE A VALID URL.
        """
        self.url = url
        self.match = re.search(
            r"^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?",
            url)

        self.scheme = self.match.group(2)
        self.authority = self.match.group(4)
        self.path = self.match.group(5)
        self.query = self.match.group(7)
        self.fragment = self.match.group(9)
        return

    def build_url(self):
        """
        Build and url the full url as a string.
        """
        if self.query is None:
            query = ""
        else:
            query = "?" + self.query

        if self.fragment is None:
            fragment = ""
        else:
            fragment = "#" + self.fragment

        built_url = self.scheme + "://" + self.authority + self.path \
            + query + fragment
        return built_url

    def set_scheme(self, scheme):
        """
        Set the local self.scheme to a new scheme type.
        """
        self.scheme = scheme
        return

    def set_authority(self, authority):
        """
        Set the local self.authority to a new authority.
        """
        self.authority = authority
        return

    def set_path(self, path):
        """
        Set the local.path to a new path.
        """
        self.path = path
        return

    def add_query(self, query):
        """
        Add a query to the query "builder"
        """
        if self.query is None:
            self.query = query
        else:
            self.query += "&" + query

        return

    def set_fragment(self, fragment):
        """
        Set the fragment of the url.
        """
        self.fragment = fragment
        return


if __name__ == "__main__":
    GOOGLE = UrlParser("https://www.google.com/test#products")
    REDDIT = UrlParser("https://reddit.com?name=example&x=2&n=4")
    RANDOM = UrlParser(
        "http://[1000::1001:1510]/web/page?userId=0123456789#fragment")

    print GOOGLE.get_scheme()
    print REDDIT.get_scheme()
    print RANDOM.get_scheme()
    print GOOGLE.get_authority()
    print REDDIT.get_authority()
    print RANDOM.get_authority()
    print GOOGLE.get_path()
    print REDDIT.get_path()
    print RANDOM.get_path()
    print GOOGLE.get_query()
    print REDDIT.get_query()
    print RANDOM.get_query()
    print GOOGLE.get_fragment()
    print REDDIT.get_fragment()
    print RANDOM.get_fragment()

    TEST = UrlBuilder()
    TEST.set_scheme("https")
    TEST.set_authority("www.example.com")
    TEST.set_path("/path/to/file")
    TEST.set_fragment("fragment")
    TEST.add_query("name=example1")
    TEST.add_query("username=example2")

    print TEST.build_url()
