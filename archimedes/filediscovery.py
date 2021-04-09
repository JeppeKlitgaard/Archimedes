"""
Contains file discovery logic.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from re import Pattern
from typing import Optional

from archimedes import ArchimedesSite
from archimedes.plugin import BasePlugin


class FileDiscoverer(ABC, BasePlugin):
    """
    A Base Class for File Discoverers.

    File Discoverers are executed sequentially in the order specified by the
    configuration.

    It is up to the individual file discoverer to ensure/modify file entries
    yielded by prior file discoverers.
    """

    file_patterns: Optional[list[Pattern[str]]] = None
    # May be used by some discoverers, but not neccessarily.

    @abstractmethod
    def discover(
        self, site: ArchimedesSite, base_dir: Path, previously_discovered: list[Path]
    ) -> list[Path]:
        """
        Run by the ArchimedesSite during the file discovery process.

        Args:
            site: The ArchimedesSite.
                Do not alter unless you know what you're doing.
            base_dir: Path to the directory containing `archi_config.py`.
            previously_discovered: A list of previously discovered paths.
        """
        ...
