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

        current_user_agent = ""
        allowed = {}
        disallowed = {}

        for line in lines:
            o_line = line
            # Get rid of all spaces in beginning of line
            while line.startswith(" "):
                line = line[1:]

            # Make the line lowercase
            line = line.lower()

            # Remove the newline at the end of each line
            line = line.rstrip()

            # Remove commented out lines
            if line.startswith("#"):
                lines.remove(o_line)

            # Create a list of list of user-agents and allow/disallow
            if line.startswith("user-agent:"):
                agent = line.split("user-agent:")[1]
                while agent.startswith(" "):
                    agent = agent[1:]

                current_user_agent = agent
            elif line.startswith("allow:"):
                allowed_path = line.split("allow:")[1]
                while allowed_path.startswith(" "):
                    allowed_path = allowed_path[1:]

                allowed.update(current_user_agent,
                               [allowed.get(current_user_agent), allowed_path])
            elif line.startswith("disallow:"):
                disallowed_path = line.split("disallow: ")[1]
                while disallowed_path.startswith(" "):
                    disallowed_path = disallowed_path[1:]

                disallowed.update(current_user_agent,
                                  [disallowed.get(current_user_agent),
                                   disallowed_path])

        for line in lines:
            print(line)

        print(current_user_agent)
        print(allowed)
        print(disallowed)

    def is_allowed(self, url):
        """
        Boolean method to determine if a given url is valid to be
        crawling the given website containing the current robots.txt
        """

        # continue here
