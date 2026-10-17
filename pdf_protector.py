"""PDF Password Protector: encrypt a PDF file with a password from the command line."""

import argparse
import getpass
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def protect_pdf(input_path, output_path, user_password, owner_password=None):
    """Create an encrypted copy of a PDF.

    user_password:  required to open the file.
    owner_password: required to change permissions (defaults to user_password).
    """
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(
        user_password=user_password,
        owner_password=owner_password or None,
        algorithm="AES-256",
    )

    with open(output_path, "wb") as f:
        writer.write(f)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Protect a PDF file with a password."
    )
    parser.add_argument("input", help="path to the PDF file to protect")
    parser.add_argument(
        "-o", "--output",
        help="output path (default: <input>_protected.pdf)",
    )
    parser.add_argument(
        "--owner-password",
        action="store_true",
        help="ask for a separate owner password",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    input_path = Path(args.input)
    if not input_path.is_file():
        sys.exit(f"Error: file not found: {input_path}")

    output_path = (
        Path(args.output)
        if args.output
        else input_path.with_name(f"{input_path.stem}_protected.pdf")
    )

    password = getpass.getpass("Enter password: ")
    if not password:
        sys.exit("Error: password cannot be empty.")
    if password != getpass.getpass("Confirm password: "):
        sys.exit("Error: passwords do not match.")

    owner = getpass.getpass("Owner password: ") if args.owner_password else None

    protect_pdf(input_path, output_path, password, owner)
    print(f"Done. Protected file saved to: {output_path}")


if __name__ == "__main__":
    main()
