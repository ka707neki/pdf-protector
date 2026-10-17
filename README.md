# 🔒 PDF Password Protector

A simple command-line tool that adds password protection to any PDF file, built with Python and [pypdf](https://pypdf.readthedocs.io/).

## ✨ Features

- **AES-256 encryption** for the output file
- **Safe password entry:** the password is typed in a hidden prompt, never stored in the code or shell history
- **Password confirmation** to avoid typos
- **Optional owner password** (controls who can change permissions)
- **Original file untouched:** a new protected copy is created

## 🚀 Getting Started

### Requirements

- Python 3.8 or newer

### Installation

```bash
git clone https://github.com/ka707neki/pdf-password-protector.git
cd pdf-password-protector
pip install -r requirements.txt
```

### Usage

```bash
python pdf_protector.py document.pdf
```

You will be asked to enter and confirm a password. The result is saved as `document_protected.pdf`.

**Options:**

| Option | Description |
|--------|-------------|
| `-o, --output PATH` | Choose the output file name |
| `--owner-password` | Ask for a separate owner password |
| `-h, --help` | Show help |

**Example:**

```bash
python pdf_protector.py report.pdf -o secure_report.pdf --owner-password
```

## 🧠 How It Works

1. `PdfReader` loads the original PDF.
2. Every page is copied into a `PdfWriter`.
3. `writer.encrypt()` applies AES-256 encryption with your password.
4. The encrypted file is written to disk.

## 🗂️ Project Structure

```
pdf-password-protector/
├── pdf_protector.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## ⚠️ Notes

- Keep your password safe: a forgotten password cannot be recovered.
- Only protect files you own or have permission to modify.

## 🛣️ Ideas for Improvement

- [ ] Remove a password from a PDF (with the correct password)
- [ ] Protect multiple files at once
- [ ] Simple GUI

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.

## 👤 Author

**ka707neki** · [GitHub](https://github.com/ka707neki)

If you like this project, a ⭐ is appreciated!
