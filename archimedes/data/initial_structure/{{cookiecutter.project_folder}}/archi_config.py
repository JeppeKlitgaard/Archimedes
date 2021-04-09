"""
This file contains the site configuration.

This file also serves as the marker for Archimedes to know where your project
root is.
"""


from archimedes.filediscovery import FileDiscoverer
from archimedes.core.filediscovery import StaticFileDiscoverer

SITE_NAME: str = "{{cookiecutter.site_name}}"


FILE_DISCOVERERS: list[FileDiscoverer] = [
    StaticFileDiscoverer(),
]
