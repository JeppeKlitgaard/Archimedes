"""
Contains core FileDiscoverers.
"""

import logging
import re
from collections.abc import Iterable
from pathlib import Path
from typing import cast

from archimedes import ArchimedesSite
from archimedes.filediscovery import FileDiscoverer
from archimedes.types import Pathlike
from archimedes.utils.path import walk_dirs

logger = logging.getLogger(__name__)


IMAGE_STATIC_EXTENSIONS = [
    "png",
    "jpg",
    "jpeg",
    "gif",
]

VIDEO_STATIC_EXTENSIONS = [
    "mov",
]

AUDIO_STATIC_EXTENSIONS = [
    "mp3",
    "ogg",
]

DOCUMENT_STATIC_EXTENSIONS = [
    "txt",
    "csv",
    # Office
    "xlsx",
    "docx",
    "pptx",
]


DEFAULT_STATIC_EXTENSIONS = (
    IMAGE_STATIC_EXTENSIONS
    + VIDEO_STATIC_EXTENSIONS
    + AUDIO_STATIC_EXTENSIONS
    + DOCUMENT_STATIC_EXTENSIONS
)


DEFAULT_STATIC_DIRS = [
    "static",
]


class StaticFileDiscoverer(FileDiscoverer):
    """
    Discovers static files.

    Should probably be placed last in the Discoverer configuration.
    """

    name = "archimedes.core.StaticFileDiscoverer"
    friendly_name = "Archimedes Core StaticFileDiscoverer"

    def __init__(
        self,
        static_dirs: Iterable[Pathlike] = DEFAULT_STATIC_DIRS,
        limit_to_extension_matching: bool = False,
        extensions: Iterable[str] = DEFAULT_STATIC_EXTENSIONS,
        matching_case_sensitive: bool = False,
    ) -> None:
        """
        Args:
            static_dirs: An iterable of directories to search in for static files
            limit_to_extension_matching: If True only files that match the
                extensions given in the `extensions` attribute will be discovered
            extensions: Iterable of strings that correspond to file extensions.
                These should NOT include the leading '.'
            matching_case_sensitive: Whether to use case sensitive matching
        """

        self.static_dirs = static_dirs
        self.limit_to_extension_matching = limit_to_extension_matching

        # We should compute file patterns
        if limit_to_extension_matching:
            self.file_patterns = []

            for extension in extensions:
                flags = 0 if matching_case_sensitive else re.IGNORECASE
                pattern = re.compile(r"^.*\." + extension, flags)
                self.file_patterns.append(pattern)

            logger.debug("Added static file patterns: %s", self.file_patterns)

    def discover(
        self, site: ArchimedesSite, base_dir: Path, previously_discovered: list[Path]
    ) -> list[Path]:
        self.file_patterns = cast(list[re.Pattern[str]], self.file_patterns)
        discovered = []

        head_dirs = [base_dir / static_dir for static_dir in self.static_dirs]
        for candidate in walk_dirs(head_dirs):
            if candidate in previously_discovered:
                continue

            if not self.limit_to_extension_matching:
                discovered.append(candidate)
                continue

            if any(
                [re.match(x, str(candidate)) is not None for x in self.file_patterns]
            ):
                discovered.append(candidate)

        return discovered
