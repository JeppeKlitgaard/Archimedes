"""
Contains path and filesystem related utilities.
"""

from collections.abc import Generator, Iterable
from pathlib import Path


# https://stackoverflow.com/questions/6639394/what-is-the-python-way-to-walk-a-directory-tree
def walk_dirs(head_dirs: Iterable[Path]) -> Generator[Path, None, None]:
    """
    Walks the subdirectories and files of a directory.

    Args:
        head_dir: Directory to walk from.
    """
    for head_dir in head_dirs:
        for p in head_dir.iterdir():
            if p.is_dir():
                yield from walk_dirs([p])
                continue

            yield p.resolve()
