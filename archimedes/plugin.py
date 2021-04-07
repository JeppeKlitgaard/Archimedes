"""
Contains base classes and logic related to plugins.

Most functionality is implemented through the use of plugins, making Archimedes very
extensible.
"""

from abc import ABC


class BasePlugin(ABC):
    name: str
    friendly_name: str
