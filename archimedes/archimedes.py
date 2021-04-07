"""
Contains the ArchimedesSite and associated logic.
"""
from typing import Optional

from archimedes.author import Author
from archimedes.compile import CompilerPlugin
from archimedes.config import ArchiTOMLConfig, SiteConfig


class ArchimedesSite:
    def __init__(
        self,
        site_config: SiteConfig,
        archi_config: ArchiTOMLConfig,
    ) -> None:

        self.site_config = site_config
        self.archi_config = archi_config
        self.compilers: list[CompilerPlugin] = []

    def resolve_author(ident: str) -> Author:
        pass
