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

        self.allowed = {}
        self.disallowed = {}

    def parse(self):
        """
        Method for parsing through and gaining information from the file.
        """
        with open(self.file_, "r") as file_:
            lines = file_.readlines()

        current_user_agent = ""
        allowed = {}
        disallowed = {}

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
        # user-agent, allow, or disallow
        for line in lines:
            if line.startswith("user-agent:"):
                current_user_agent = line.split(": ")[1]
            elif line.startswith("allow:"):
                if allowed.get(current_user_agent) is None:
                    allowed[current_user_agent] = line.split(": ")[1]
                else:
                    allowed[current_user_agent] = list(allowed.get(
                        current_user_agent)) + [line.split(": ")[1]]
            elif line.startswith("disallow:"):
                if disallowed.get(current_user_agent) is None:
                    disallowed[current_user_agent] = line.split(": ")[1]
                else:
                    disallowed[current_user_agent] = list(disallowed.get(
                        current_user_agent)) + [line.split(": ")[1]]

        self.allowed = allowed
        self.disallowed = disallowed

        print(self.allowed)
        print(self.disallowed)

        return True
