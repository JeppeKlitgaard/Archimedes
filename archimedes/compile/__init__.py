"""
Contains base code for compilers.

All compilers, even the default ones, are implemented as plugins.
"""

from abc import abstractmethod
from io import RawIOBase

from archimedes.plugin import BasePlugin


class CompilerPlugin(BasePlugin):
    @abstractmethod
    def compile(self, src: str) -> str:
        ...
