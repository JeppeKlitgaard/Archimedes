"""
This contains the default configuration values.
"""

from archimedes.filediscovery import FileDiscoverer
from archimedes.core.filediscovery import StaticFileDiscoverer

SITE_NAME: str = "Archimedes' Bathtub"

FILE_DISCOVERERS: list[FileDiscoverer] = [
    StaticFileDiscoverer(),
]
