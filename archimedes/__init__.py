"""
Archimedes is an opinionated static site generator geared
towards personal websites and microblogs.
"""

from archimedes.compile import CompilerPlugin


class ArchimedesSite:
    def __init__(self) -> None:
        self.compilers: list[CompilerPlugin] = []
