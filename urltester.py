#!/usr/bin/env python3
"""
Class for testing the UrlParser and UrlBuilder classes.
(scheme://)([userInfo@]authority[:port])[/path/to/file][?query][#fragment]
"""
from urlparser import UrlParser
from urlbuilder import UrlBuilder


if __name__ == "__main__":
    GOOGLE = UrlParser("https://www.google.com:8000/test#products")
    REDDIT = UrlParser("account_1@github.com?name=example&x=2&n=4")
    RANDOM = UrlParser(
        "http://[1000::1001:1510]/web/page?userId=0123456789#fragment")

    print(GOOGLE.get_scheme())
    print(REDDIT.get_scheme())
    print(RANDOM.get_scheme())
    print(GOOGLE.get_authority())
    print(REDDIT.get_authority())
    print(RANDOM.get_authority())
    print(GOOGLE.get_path())
    print(REDDIT.get_path())
    print(RANDOM.get_path())
    print(GOOGLE.get_query())
    print(REDDIT.get_query())
    print(RANDOM.get_query())
    print(GOOGLE.get_fragment())
    print(REDDIT.get_fragment())
    print(RANDOM.get_fragment())

    TEST = UrlBuilder()
    TEST.set_authority("www.example.com")
    TEST.set_path("/path/to/file")
    TEST.set_scheme("https")
    TEST.set_fragment("fragment")
    TEST.add_query("name=example1")
    TEST.add_query("username=example2")

    print(TEST.build_url())

    # print(GOOGLE.is_valid())
    # print(REDDIT.is_valid())
    # print(RANDOM.is_valid())
    # finishing implementation of is_valid for both urlparser and urlbuilder
    # add .gitignore for __pycache__/
