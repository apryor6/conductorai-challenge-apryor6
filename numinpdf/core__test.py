"""Core Tests"""

import pytest
from numinpdf.test import text_to_pdf
from click.testing import CliRunner

from .core import numinpdf, _numinpdf


@pytest.fixture()
def temp_pdf_file(tmp_path):
    """Helper fixture for creating a temporary PDF file. Each test will write its own content"""
    f1 = tmp_path / "mydir/myfile.pdf"
    f1.parent.mkdir()
    f1.touch()
    full_filename = f1.absolute()
    return str(full_filename)


def test_numinpdf__42(temp_pdf_file):
    """numinpdf should return 42 when it is the largest number in the PDF."""
    # Arrange
    text_to_pdf("test there is a 42", temp_pdf_file)

    # Act
    result = _numinpdf(temp_pdf_file)

    # Assert
    assert result == 42


def test_numinpdf__4(temp_pdf_file):
    """numinpdf should return 4 when it is the largest number in the PDF."""
    text_to_pdf("test there is 1 and also a 4", temp_pdf_file)
    result = _numinpdf(temp_pdf_file)
    assert result == 4


def test_numinpdf__with_commas(temp_pdf_file):
    """numinpdf should return the correct number when it is comma separated"""
    text_to_pdf("9999 is a pretty large number but it is not as large as 123,456,789,000", temp_pdf_file)
    result = _numinpdf(temp_pdf_file)
    assert result == 123456789000


def test_numinpdf_cli_runner(temp_pdf_file):
    """Test the CLI runner for numinpdf"""
    runner = CliRunner()
    text_to_pdf("You know nothing, John Snow", temp_pdf_file)

    result = runner.invoke(numinpdf, [temp_pdf_file])
    assert result.exit_code == 0
