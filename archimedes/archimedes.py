"""
Contains the ArchimedesSite and associated logic.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from archimedes.author import Author
    from archimedes.config import SiteConfig


class ArchimedesSite:
    def __init__(
        self,
        site_config: SiteConfig,
        project_active: bool,
    ) -> None:

        self.site_config = site_config
        self.project_active = project_active

    def resolve_author(self, ident: str) -> Author:
        pass
