from .core import _numinpdf  # Replace with actual function names and imports


def test_numinpdf():
    # Arrange
    filename = "TestyMcTestfile.pdf"

    # Act
    result = _numinpdf(filename)

    # Assert
    assert result is None
