#!/usr/bin/env python3
"""
Class for testing the UrlParser and UrlBuilder classes.
(scheme://)([userInfo@]authority[:port])[/path/to/file][?query][#fragment]
"""
import unittest
from robotparser import RobotParser
from urlparser import UrlParser
from urlbuilder import UrlBuilder


class TestUrlParser(unittest.TestCase):
    """
    Unit tests for the UrlParser class.
    """
    url = UrlParser(
        "https://user:pass@www.google.com:8000/path/to/file?one=1&two=2#prod")

    def test_valid(self):
        assert self.url.is_valid()

    def test_scheme(self):
        assert self.url.get_scheme() == "https"

    def test_authority(self):
        assert self.url.get_authority() == "user:pass@www.google.com:8000"

    def test_path(self):
        assert self.url.get_path() == "/path/to/file"

    def test_query(self):
        assert self.url.get_query() == "one=1&two=2"

    def test_fragment(self):
        assert self.url.get_fragment() == "prod"

    def test_file(self):
        assert self.url.get_file() == "file"

    def test_username(self):
        assert self.url.get_username() == "user"

    def test_password(self):
        assert self.url.get_password() == "pass"

    def test_hostname(self):
        assert self.url.get_hostname() == "www.google.com"

    def test_port(self):
        assert self.url.get_port() == "8000"


class TestUrlBuilder(unittest.TestCase):
    """
    Unit tests for the UrlBuilder class.
    """
    url = UrlBuilder()
    url.set_authority("www.example.com").set_path("/path/to/file")
    url.set_scheme("https").set_fragment("fragment")
    url.add_query("name=example1").add_query("username=example2")

    def test_valid(self):
        assert self.url.is_valid()

    def test_build(self):
        assert (self.url.build_url() ==
                "https://www.example.com/path/to/file?name=example"
                "1&username=example2#fragment")


class TestRobotParser(unittest.TestCase):
    """
    Unit tests for the RobotParser class.
    """
    robot = RobotParser("test_robots.txt")
    user_agent1 = "MJ12bot".lower()
    user_agent2 = "Mediapartners-Google*".lower()

    robot.parse()

    def test_parse(self):
        assert self.robot.parse()

    def test_is_allowed(self):
        assert self.robot.is_allowed(self.user_agent1, "/path/to/file.index")

    def test_is_disallowed(self):
        assert self.robot.is_disallowed(self.user_agent2, "/")

    def test_crawl_delay(self):
        assert self.robot.get_crawl_delay(self.user_agent1) == 6

    def test_request_rate(self):
        assert self.robot.get_request_rate(self.user_agent2) == 4

    def test_sitemap(self):
        assert self.robot.get_sitemap(self.user_agent2) == "/path/to/sitemap"


if __name__ == "__main__":
    unittest.main()
