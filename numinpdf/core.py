"""Core numinpdf functionality"""

from numbers import Number
import re

import PyPDF2
import click


def find_largest_number_in_pdf(filename: str) -> Number | None:
    """
    Finds the largest number in a PDF file.

    Args:
        filename (str): The path to the PDF file.

    Returns:
        float: The largest number found in the PDF, or None if no number is found.
    """
    try:
        with open(filename, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text().replace(",", "")
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return None
    except PyPDF2.errors.PdfReadError:
        print(f"Error: Could not read pdf: {filename}")
        return None

    # The regex pattern r"-?\d+(?:\.\d+)?(?:[mbMB])?" is designed to match numbers with
    # optional decimal points and optional magnitude suffixes (like 'm' or 'b').
    # Here's a breakdown of the pattern:
    # -?: Matches an optional minus sign, allowing for negative numbers.

    # \d+: Matches one or more digits.

    # (?:\.\d+)?: Matches an optional non-capturing group that consists of a decimal point followed by one or
    #   more digits.

    # (?:[mbMB])?: Matches an optional non-capturing group that consists of either 'm', 'b', 'M', or 'B',
    #   which could represent magnitude suffixes like million or billion.

    # This pattern will match integers, floating-point numbers, negative numbers, and numbers with optional
    # magnitude suffixes.
    NUMBER_REGEX = r"-?\d+(?:\.\d+)?(?:[mbkMBK])?"
    matches = re.findall(NUMBER_REGEX, text)
    numbers = [_handle_token(token) for token in matches]
    return max(numbers) if numbers else None


def _handle_token(token: str) -> str:
    """Helper function for parsing tokens that is capable of converting suffixes into the appropriate multiplier"""
    FACTORS = {"k": 1_000, "K": 1_000, "m": 1_000_000, "M": 1_000_000, "b": 1_000_000_000, "B": 1_000_000_000}
    for k, v in FACTORS.items():
        if k in token:
            # Note: this does not guard for 'malformed' suffixes like '1.5Mm' and would result
            # in TypeErrors etc that I have not guarded for
            return float(token.replace(k, "")) * v
    return float(token)


def _numinpdf(filename: str):
    """
    Finds the largest number in a PDF file.

    Args:
        filename (str): The path to the PDF file.

    Returns:
        None, prints the largest number found in the PDF, or a message if no number is found.
    """
    largest_number = find_largest_number_in_pdf(filename)

    if largest_number is not None:
        print(f"The largest number in {filename} is: {largest_number}")
    else:
        print(f"No numbers found in {filename}.")
    return largest_number


@click.command()
@click.argument("filename", default="data/FY25 Air Force Working Capital Fund.pdf")
def numinpdf(filename: str):
    """Click wrapper to create a CLI for main entrypoint

    Usage: `numinpdf <filename>` (or with uv `uv run numinpdf <filename>`)
    """
    _numinpdf(filename)
