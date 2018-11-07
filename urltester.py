#!/usr/bin/env python3
"""
Class for testing the UrlParser and UrlBuilder classes.
(scheme://)([userInfo@]authority[:port])[/path/to/file][?query][#fragment]
"""
import unittest
from urlparser import UrlParser
from urlbuilder import UrlBuilder
from robotparser import RobotParser


class TestUrlParser(unittest.TestCase):
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
    url = UrlBuilder()
    url.set_authority("www.example.com").set_path("/path/to/file")
    url.set_scheme("https").set_fragment("fragment")
    url.add_query("name=example1")
    url.add_query("username=example2")

    def test_valid(self):
        assert self.url.is_valid()

    def test_build(self):
        assert (self.url.build_url() ==
                "https://www.example.com/path/to/file?name=example"
                "1&username=example2#fragment")


if __name__ == "__main__":
    RobotParser("test_robots.txt").parse()
    unittest.main()
