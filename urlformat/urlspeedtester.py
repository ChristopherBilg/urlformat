#!/usr/bin/env python3
"""
Class for testing the speed of specific classes.
"""
import datetime
from robotparser import RobotParser
from urlparser import UrlParser
from urlbuilder import UrlBuilder


class SpeedTestUrlParser:
    """
    Speed tests for the UrlParser class.
    """

    @staticmethod
    def test(itterations):
        start_time = datetime.datetime.now()
        for _ in range(itterations):
            url = UrlParser("https://www.google.com/path/to?one=1&two=2#frag")
            url = url.get_scheme() + url.get_authority()
        end_time = datetime.datetime.now()

        return end_time - start_time


class SpeedTestUrlBuilder:
    """
    Speed tests for the UrlBuilder class.
    """

    @staticmethod
    def test(itterations):
        start_time = datetime.datetime.now()
        for _ in range(itterations):
            url = UrlBuilder().set_scheme("https")
            url.set_authority("www.google.com").set_path("/path/to")
            url.add_query("one=1").add_query("two=2").set_fragment("frag")
        end_time = datetime.datetime.now()

        return end_time - start_time


class SpeedTestRobotParser:
    """
    Speed tests for the RobotParser class.
    """

    @staticmethod
    def test(itterations):
        start_time = datetime.datetime.now()
        for _ in range(itterations):
            robot = RobotParser("test_robots.txt")
            robot.parse()
        end_time = datetime.datetime.now()

        return end_time - start_time


if __name__ == "__main__":
    ITTER = 1000000  # Itterations = 1 million
    print("Testing over 1,000,000 itterations:")

    URL_P = SpeedTestUrlParser.test(ITTER)
    print("UrlParser: " + str(URL_P))

    URL_B = SpeedTestUrlBuilder.test(ITTER)
    print("UrlBuilder: " + str(URL_B))

    ROBOT_P = SpeedTestRobotParser.test(ITTER)
    print("RobotParser: " + str(ROBOT_P))
