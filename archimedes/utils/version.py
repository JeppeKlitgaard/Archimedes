from pathlib import Path

import toml
from semantic_version import Version


def get_version() -> Version:
    """
    Returns the version of Archimedes.
    """

    main_path = Path(__file__).resolve().parents[2]  # /archimedes/
    # Note this depends on where this module is located within Archimedes

    pyproject = toml.load(main_path / "pyproject.toml")

    return pyproject["tool"]["poetry"]["version"]
