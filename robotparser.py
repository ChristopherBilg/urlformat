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
            raise TypeError
        self.file_ = file_

    def parse(self):
        """
        Method for parsing through and gaining information from the file.
        """
        with open(self.file_, "r") as f:
            lines = f.readlines()

        print(lines)
