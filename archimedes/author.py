"""
Contains the Author model and associated logic.
"""
from __future__ import annotations

from typing import Type

from pydantic import BaseModel, EmailStr, Field


class Author(BaseModel):
    ident: str
    aliases: list[str] = Field(
        default_factory=list,
        description="A list of other identities to resolve the author from.",
    )
    first_name: str
    last_name: str
    e_mail: EmailStr

    @classmethod
    def from_ident(cls: Type[Author], ident: str, accept_alises: bool = True) -> Author:
        pass
