#!/usr/bin/env python3
"""
Class for parsing through robots.txt files.
"""


class RobotParser:
    """
    Class for parsing through robots.txt files.
    """
    def __init__(self, file_=None):
        """
        Initialization method.
        """
        if file_ is None:
            raise TypeError("No valid file has been given.")
        self.file_ = file_

    def parse(self):
        """
        Method for parsing through and gaining information from the file.
        """
        with open(self.file_, "r") as file_:
            lines = file_.readlines()

        print(lines)

        # continue here

    def is_allowed(self, url):
        """
        Boolean method to determine if a given url is valid to be
        crawling the given website containing the current robots.txt
        """

        # continue here
