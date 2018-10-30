#!/usr/bin/env python3
"""
Class for building valid urls.
"""


import re


class UrlBuilder():
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

    def build_url(self):
        """
        Build the full url as a string.
        """
        if self.query is None:
            query = ""
        else:
            query = "?" + self.query

        if self.fragment is None:
            fragment = ""
        else:
            fragment = "#" + self.fragment

        if self.scheme is None:
            scheme = ""
        else:
            scheme = self.scheme + "://"

        built_url = scheme + self.authority + self.path + query + fragment
        return built_url

    def set_scheme(self, scheme):
        """
        Set the local self.scheme to a new scheme type.
        """
        self.scheme = scheme

    def set_authority(self, authority):
        """
        Set the local self.authority to a new authority.
        """
        self.authority = authority

    def set_path(self, path):
        """
        Set the local.path to a new path.
        """
        self.path = path

    def add_query(self, query):
        """
        Add a query to the query "builder"
        """
        if self.query is None:
            self.query = query
        else:
            self.query += "&" + query

    def set_fragment(self, fragment):
        """
        Set the fragment of the url.
        """
        self.fragment = fragment


if __name__ == "__main__":
    print("To use this package, please import it into your python script.")
