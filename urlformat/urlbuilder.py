#!/usr/bin/env python3
"""
Class for building valid urls.
"""
import re
from urlformat.errors import UnbuiltURLError


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
            r"^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?", url)

        self.scheme = self.match.group(2)
        self.authority = self.match.group(4)
        self.path = self.match.group(5)
        self.query = self.match.group(7)
        self.fragment = self.match.group(9)

    def __repr__(self):
        """
        Formal string representation of the url.
        """
        return self.build_url()

    def __str__(self):
        """
        Informal string representation of the url.
        """
        return self.build_url()

    def __len__(self):
        """
        Implementation of the len() method.
        """
        return len(self.build_url())

    def build_url(self, check_validity=True):
        """
        Build the full url as a string.
        """
        if self.scheme is None:
            scheme = ""
        else:
            scheme = self.scheme + "://"

        if self.authority is None:
            authority = ""
        else:
            authority = self.authority

        if self.path is None:
            path = ""
        else:
            path = self.path

        if self.query is None:
            query = ""
        else:
            query = "?" + self.query

        if self.fragment is None:
            fragment = ""
        else:
            fragment = "#" + self.fragment

        built_url = scheme + authority + path + query + fragment

        if check_validity:
            if not self.is_valid():
                raise UnbuiltURLError(
                    "The given url is not a valid url of form:\n"
                    "\t(scheme://)([userInfo@]authority[:port])"
                    "[/path/to/file][?query][#fragment]")

        return built_url

    def set_scheme(self, scheme):
        """
        Set the local self.scheme to a new scheme type.
        """
        self.scheme = scheme
        return self

    def set_authority(self, authority):
        """
        Set the local self.authority to a new authority.
        """
        self.authority = authority
        return self

    def set_path(self, path):
        """
        Set the local.path to a new path.
        """
        self.path = path
        return self

    def add_query(self, query):
        """
        Add a query to the query "builder"
        """
        if self.query is None:
            self.query = query
        else:
            self.query += "&" + query

        return self

    def set_fragment(self, fragment):
        """
        Set the fragment of the url.
        """
        self.fragment = fragment
        return self

    def is_valid(self):
        """
        Boolean method for obtaining the validity of the built url.
        """
        return self.scheme is not None and self.authority is not None


if __name__ == "__main__":
    print("To use this package, please import it into your python script.")
