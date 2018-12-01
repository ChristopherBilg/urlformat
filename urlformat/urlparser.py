#!/usr/bin/env python3
"""
Parser class for parsing through web urls.
"""
import re
from urlformat.errors import InvalidURLError


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
            r"^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?", url)

        if not self.is_valid():
            raise InvalidURLError("The given url is not valid: " +
                                  self.match.group(0))

    def __repr__(self):
        """
        Formal string representation of the url.
        """
        return self.match.group(0)

    def __str__(self):
        """
        Informal string representation of the url.
        """
        return self.match.group(0)

    def __len__(self):
        """
        Implementation of the len() method.
        """
        return len(self.match.group(0))

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
        # return None if self.match.group(5) == "" else self.match.group(5)
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
        return (self.match.group(2) is not None
                and self.match.group(4) is not None)

    def get_file(self):
        """
        Getter method for the file at the end of the path.
        """
        if "/" in self.match.group(5):
            return self.match.group(5).split("/")[-1]

        return self.match.group(5)

    def get_username(self):
        """
        Getter method for the username in the URL authority.
        """
        if "@" in self.match.group(4):
            if ":" in self.match.group(4).split("@")[0]:
                return self.match.group(4).split("@")[0].split(":")[0]
            return self.match.group(4).split("@")[0]

        return ""

    def get_password(self):
        """
        Getter method for the password in the URL authority.
        """
        if "@" in self.match.group(4):
            if ":" in self.match.group(4).split("@")[0]:
                return self.match.group(4).split("@")[0].split(":")[1]
            return ""

        return ""

    def get_hostname(self):
        """
        Getter method for the hostname in the URL authority.
        """
        if "@" in self.match.group(4):
            if ":" in self.match.group(4).split("@")[1]:
                return self.match.group(4).split("@")[1].split(":")[0]
            return self.match.group(4).split("@")[1]

        if ":" in self.match.group(4):
            return self.match.group(4).split(":")[0]
        return self.match.group(4)

    def get_port(self):
        """
        Getter method for the port in the URL authority.
        """
        if "@" in self.match.group(4):
            if ":" in self.match.group(4).split("@")[1]:
                return self.match.group(4).split("@")[1].split(":")[1]
            return ""

        if ":" in self.match.group(4):
            return self.match.group(4).split(":")[1]
        return ""


if __name__ == "__main__":
    print("To use this package, please import it into your python script.")
