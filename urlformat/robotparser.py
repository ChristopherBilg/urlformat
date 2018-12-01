#!/usr/bin/env python3
"""
Class for parsing through robots.txt files.
"""
from urlformat.errors import RobotNotFoundError


class RobotParser:
    """
    Class for parsing through robots.txt files.
    """

    def __init__(self, file_=None):
        """
        Initialization method.
        """
        if file_ is None:
            raise RobotNotFoundError("No valid file has been given.")
        self.file_ = file_

        self.allowed = {}
        self.disallowed = {}
        self.crawl_delays = {}
        self.request_rates = {}
        self.sitemaps = {}

    def parse(self):
        """
        Method for parsing through and gaining information from the file.
        """
        with open(self.file_, "r") as file_:
            lines = file_.readlines()

        current_user_agent = ""
        allowed = {}
        disallowed = {}
        crawl_delays = {}
        request_rates = {}
        sitemaps = {}

        # Get rid of all spaces in beginning of line
        for index, line in enumerate(lines):
            while line.startswith(" "):
                lines[index] = line[1:]

        # Get rid of ending newline
        for index, line in enumerate(lines):
            lines[index] = line.strip("\n")

        # Get ride of all spaces in the end of the line
        for index, line in enumerate(lines):
            while line.endswith(" "):
                lines[index] = line[:-1]

        # Make the entire line lowercase
        for index, line in enumerate(lines):
            lines[index] = line.lower()

        # Remove blank lines
        for index, line in enumerate(lines):
            if line == "":
                del lines[index]

        # Check for one of three beginning states
        # user-agent, allow, disallow, crawl-delay, request-rate, sitemap
        for line in lines:
            if line.startswith("user-agent:"):
                current_user_agent = line.split(": ")[1]
            elif line.startswith("allow:"):
                if allowed.get(current_user_agent) is None:
                    allowed[current_user_agent] = line.split(": ")[1]
                else:
                    allowed[current_user_agent] = list(
                        allowed.get(current_user_agent)) + list(
                            line.split(": ")[1])
            elif line.startswith("disallow:"):
                if disallowed.get(current_user_agent) is None:
                    disallowed[current_user_agent] = line.split(": ")[1]
                else:
                    disallowed[current_user_agent] = list(
                        disallowed.get(current_user_agent)) + list(
                            line.split(": ")[1])
            elif line.startswith("crawl-delay:"):
                if line.split(": ")[1].isnumeric():
                    crawl_delays[current_user_agent] = line.split(": ")[1]
            elif line.startswith("request-rate:"):
                if line.split(": ")[1].isnumeric():
                    request_rates[current_user_agent] = line.split(": ")[1]
            elif line.startswith("sitemap:"):
                sitemaps[current_user_agent] = line.split(": ")[1]

        self.allowed = allowed
        self.disallowed = disallowed
        self.crawl_delays = crawl_delays
        self.request_rates = request_rates
        self.sitemaps = sitemaps

        return True

    def is_allowed(self, user_agent, path):
        """
        Boolean method for determining if a given user_agent
        is allowed to access a given path.
        """
        if user_agent not in self.allowed.keys():
            return False

        if path not in self.allowed.get(user_agent):
            return False

        return True

    def is_disallowed(self, user_agent, path):
        """
        Boolean method for determining if a given user_agent
        is disallowed from accessing a given path.
        """
        if user_agent not in self.disallowed.keys():
            return False

        if path not in self.disallowed.get(user_agent):
            return False

        return True

    def get_crawl_delay(self, user_agent):
        """
        Getter method for the crawl delay for a specific user_agent.
        Returns 0 if none is specified.
        """
        if user_agent in self.crawl_delays.keys():
            return int(self.crawl_delays.get(user_agent))

        return 0

    def get_request_rate(self, user_agent):
        """
        Getter method for the request rate for a specific user_agent.
        Returns 0 if none is specified.
        """
        if user_agent in self.request_rates.keys():
            return int(self.request_rates.get(user_agent))

        return 0

    def has_sitemap(self, user_agent):
        """
        Boolean method for determining is a given user_agent
        has access to a sitemap for the current robots.txt file.
        """
        return user_agent in self.sitemaps.keys()

    def get_sitemap(self, user_agent):
        """
        Getter method for the sitemap given a specific user_agent.
        """
        if user_agent in self.sitemaps.keys():
            return self.sitemaps.get(user_agent)

        raise RuntimeError("There is not a sitemap for the given user_agent.")
