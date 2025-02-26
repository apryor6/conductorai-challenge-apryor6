from numbers import Number
import PyPDF2
import re
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
                text += page.extract_text()
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return None
    except PyPDF2.errors.PdfReadError:
        print(f"Error: Could not read pdf: {filename}")
        return None

    # This pattern will match numbers with commas as thousand separators, as well as integers, floating-point
    # numbers, and negative numbers. The replace(',', '') method is used to remove commas from the matched
    # numbers before converting them to floats.
    NUMBER_REGEX = r"-?\d{1,3}(?:,\d{3})*(?:\.\d+)?"
    numbers = [float(num.replace(",", "")) for num in re.findall(NUMBER_REGEX, text) if num]

    if numbers:
        return max(numbers)
    else:
        return None


def _numinpdf(filename: str):
    """
    Finds the largest number in a PDF file.

    Args:
        filename (str): The path to the PDF file.

    Returns:
        None, prints the largest number found in the PDF, or a message if no number is found.
    """
    # filename = "data/FY25 Air Force Working Capital Fund.pdf"
    # largest_number = find_largest_number_in_pdf(filename)
    largest_number = find_largest_number_in_pdf(filename)

    if largest_number is not None:
        print(f"The largest number in {filename} is: {largest_number}")
    else:
        print(f"No numbers found in {filename}.")


@click.command()
@click.argument("filename", default="data/FY25 Air Force Working Capital Fund.pdf")
def numinpdf(filename: str):
    """Click wrapper to create a CLI for main entrypoint

    Usage: `numinpdf <filename>` (or with uv `uv run numinpdf <filename>`)
    """
    _numinpdf(filename)
