import pytest

from archimedes.errors import MetadataException
from archimedes.metadata import MetafileExtractor
from archimedes.page import RawPage


def test_no_file(nonexistant_file):
    page = RawPage()

    page.src_filepath = nonexistant_file

    extractor = MetafileExtractor()

    with pytest.raises(MetadataException):
        extractor.extract(page)


def test_good_meta(test_dir):
    page = RawPage()
    page.src_filepath = test_dir / "metadata" / "data" / "good.md"

    extractor = MetafileExtractor()
    extractor.extract(page)
