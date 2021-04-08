"""
Contains base classes and logic related to plugins.

Most functionality is implemented through the use of plugins, making Archimedes very
extensible.
"""

from abc import ABCMeta


class BasePlugin(ABCMeta):
    name: str
    friendly_name: str

    def __init__(self) -> None:
        ...
