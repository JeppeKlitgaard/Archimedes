"""
Contains base code for compilers.

All compilers, even the default ones, are implemented as plugins.
"""

from archimedes.plugin import BasePlugin


class CompilerPlugin(BasePlugin):
    name: str
    friendly_name: str

    pass
