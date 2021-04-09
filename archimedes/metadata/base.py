from __future__ import annotations

from abc import abstractmethod
from datetime import datetime
from typing import MutableMapping, Optional, cast

from pydantic import BaseModel, Field

from archimedes.author import Author
from archimedes.errors import MetadataException
from archimedes.page import RawPage
from archimedes.plugin import BasePlugin
from archimedes.types import RawMetaValue


class Metadata(BaseModel):
    title: str = Field(..., max_length=100)
    authors: list[Author]
    publish_date: datetime
    last_update_date: datetime
    expiry_date: Optional[datetime]
    draft: bool = False

    @classmethod
    def from_raw_dict(
        cls: type[Metadata], raw_dict: MutableMapping[str, RawMetaValue]
    ) -> Metadata:

        # Manually resolve Authors
        if not raw_dict.get("authors"):
            raise MetadataException(
                "At least 1 author must be set in metadata under key: 'authors'."
            )

        raw_authors = cast(list[str], raw_dict["authors"])
        authors = [
            Author.from_ident(ident, accept_alises=True) for ident in raw_authors
        ]

        raw_dict["authors"] = authors
        return Metadata.parse_obj(raw_dict)


class MetadataExtractorPlugin(BasePlugin):
    @abstractmethod
    def extract(self, page: RawPage) -> Metadata:
        ...
