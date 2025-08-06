# Python Password Analyzer Tool

A powerful command-line tool to analyze password strength, generate strong passwords, and scan files for weak credentials.

This tool is designed with **privacy first**. All analysis is performed locally on your machine; no passwords are ever sent over the network.

## Features

- **Strength Check**: Analyzes a single password using `zxcvbn` to calculate its entropy and estimate crack time.
- **Strong Suggestions**: Generates either memorable passphrases (e.g., `rocket-shadow-winter-apple`) or cryptographically secure random passwords.
- **Bulk Scanning**: Scans a text file with one password per line and generates a report highlighting weak passwords and suggesting stronger alternatives.

## Setup

1.  **Prerequisites**: Make sure you have Python 3.7+ installed.
2.  **Clone the repository** (or download the files).
3.  **Install dependencies**: Navigate to the project directory in your terminal and run:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The tool is run from the command line.

### 1. Analyze a Single Password

Use the `-p` or `--password` flag.

```bash
python password_analyzer.py -p "password123"
```
 <!-- You can add a screenshot here -->

### 2. Generate a Strong Password

Use the `-g` or `--generate` flag. By default, it creates a memorable passphrase.

```bash
# Generate a passphrase (default)
python password_analyzer.py -g

# Generate a 20-character random password
python password_analyzer.py -g --type random --length 20
```

### 3. Scan a File for Weak Passwords

Use the `-s` or `--scan` flag, followed by the path to your file.

Create a file named `my_passwords.txt` with content like:
```
123456
monkey
P@ssw0rdStr0ng!
qwerty
my-super-secret-password-123
```

Now, run the scan:
```bash
python password_analyzer.py -s my_passwords.txt
```

The tool will output a clean, color-coded table showing only the weak passwords found and suggesting replacements.

 <!-- You can add a screenshot here -->

## Privacy Disclaimer

This script operates **100% offline and locally**. Your passwords are not stored, logged, or transmitted anywhere. The analysis is done entirely within the script's execution on your computer.
