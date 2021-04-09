"""
This file contains the site configuration.

This file also serves as the marker for Archimedes to know where your project
root is.
"""


from archimedes.core.filediscovery import StaticFileDiscoverer
from archimedes.filediscovery import FileDiscoverer

SITE_NAME: str = "{{cookiecutter.site_name}}"


FILE_DISCOVERERS: list[FileDiscoverer] = [
    StaticFileDiscoverer(),
]
