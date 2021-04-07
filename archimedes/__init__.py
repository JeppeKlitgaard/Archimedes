"""
Archimedes is an opinionated static site generator geared
towards personal websites and microblogs.
"""

import archimedes.log  # noqa
from archimedes.archimedes import ArchimedesSite
from archimedes.utils.version import get_version as __get_version

__version__ = __get_version()

__all__ = ["ArchimedesSite"]
