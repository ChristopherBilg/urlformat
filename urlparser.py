#!/usr/bin/env python3
"""
Parser class for parsing through web urls.
"""
import re


class UrlParser():
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

    def __repr__(self):
        """
        Formal string representation of the url.
        """
        return self.get_url()

    def __str__(self):
        """
        Informal string representation of the url.
        """
        return self.get_url()

    def __len__(self):
        """
        Implementation of the len() method.
        """
        return len(self.get_url())

    def get_url(self):
        """
        Getter method for the url itself.
        """
        return self.match.group(0)

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

    def is_valid(self):
        """
        Boolean method for obtaining the validity of the parsed url.
        """
        if self.match.group(2) is not None and self.match.group(4) is not None:
            return True
        return False


if __name__ == "__main__":
    print("To use this package, please import it into your python script.")
