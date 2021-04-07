"""
Contains errors and exceptions for Archimedes.
"""


class ArchimedesException(Exception):
    pass


class PageException(ArchimedesException):
    pass


class MetadataException(PageException):
    pass
