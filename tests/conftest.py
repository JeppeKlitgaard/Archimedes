import os
from pathlib import Path

import pytest


@pytest.fixture
def nonexistant_file() -> Path:
    filepath = Path("/tmp/file_that_does_not_exist_ever_lalalala")
    assert not filepath.exists()

    return filepath


@pytest.fixture
def test_dir() -> Path:
    return Path(__file__).absolute().parent
