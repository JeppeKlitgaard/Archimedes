"""
Contains code for extracting metadata using a separate .meta file.
"""

import toml

from archimedes.errors import MetadataException
from archimedes.metadata.base import Metadata, MetadataExtractorPlugin
from archimedes.page import RawPage


class MetafileExtractor(MetadataExtractorPlugin):
    def extract(self, page: RawPage) -> Metadata:
        meta_filepath = page.src_filepath.with_suffix(".meta")

        if not meta_filepath.exists():
            raise MetadataException(
                f"Could not find metadata file for page {page}. "
                "Please specify metadata for page in '{meta_filepath}' "
                "or use an alternative metadata method."
            )

        # File exists, read it using toml

        with open(meta_filepath, "r") as f:
            metadata_str = f.read()

        metadata_raw = toml.load(meta_filepath)

        return Metadata.from_raw_dict(metadata_raw)
