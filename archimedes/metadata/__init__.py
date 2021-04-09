"""
Contains metadata-related code.
"""

from archimedes.metadata.base import Metadata, MetadataExtractorPlugin  # noqa
from archimedes.metadata.meta_file import MetafileExtractor  # noqa

__all__ = [
    "Metadata",
    "MetadataExtractorPlugin",
    "MetafileExtractor",
]
