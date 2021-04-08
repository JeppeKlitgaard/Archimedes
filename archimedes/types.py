"""
Contain types used by Archimedes.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Union

RawMetaValue = Union[str, int, list[Any], dict[str, Any]]
# Ideally we would want the one below, but mypy does not yet support
# recursive types.
# see: https://github.com/python/mypy/issues/731
# RawMetaValue = Union[str, int, list[RawMetaValue], dict[str, RawMetaValue]]

Pathlike = Union[Path, str]
