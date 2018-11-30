#!/usr/bin/env python3
"""
Class for parsing through sitemap.xml files.
"""


class SitemapParser:
    """
    Class for parsing through sitemap.xml files.
    """

    def __init__(self, file_=None):
        """
        Initialization method.
        """
        if file_ is None:
            raise TypeError("No valid file has been given.")
        self.file_ = file_
