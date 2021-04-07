"""
Contains the Page class and associated logic.
"""

from pathlib import Path


class RawPage:
    src_filepath: Path

    def __repr__(self) -> str:
        return f"<archimedes.page.RawPage at '{self.src_filepath}'>"


class RenderedPage:
    pass
