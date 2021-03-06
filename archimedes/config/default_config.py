"""
This contains the default configuration values.
"""

from archimedes.command.base import ArchimedesTaskLoader
from archimedes.core.filediscovery import StaticFileDiscoverer
from archimedes.filediscovery import FileDiscoverer

SITE_NAME: str = "Archimedes' Bathtub"

FILE_DISCOVERERS: list[FileDiscoverer] = [
    StaticFileDiscoverer(),
]

TASK_LOADER: type[ArchimedesTaskLoader] = ArchimedesTaskLoader
