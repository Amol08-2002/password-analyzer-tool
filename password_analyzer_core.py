import secrets
import string
from pathlib import Path

from rich.console import Console
from rich.table import Table
from zxcvbn import zxcvbn

# This file contains the core logic for the password analyzer.
# It is designed to be imported by another script.

console = Console()

WORDLIST = [
    'apple', 'banana', 'galaxy', 'mountain', 'ocean', 'python', 'rocket',
    'shadow', 'sunset', 'waterfall', 'whisper', 'winter', 'bridge', 'candle',
]

def generate_random_password(length: int = 16) -> str:
    """Generates a cryptographically secure random password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def generate_passphrase(num_words: int = 4, separator: str = '-') -> str:
    """Generates a memorable passphrase using a wordlist."""
    words = [secrets.choice(WORDLIST) for _ in range(num_words)]
    return separator.join(words)

def analyze_password_strength(password: str):
    """Analyzes a single password and prints a detailed report."""
    if not password:
        console.print("[bold red]Error: Password cannot be empty.[/bold red]")
        return

    results = zxcvbn(password)
    score = results['score']
    
    color = "red" if score < 2 else "yellow" if score < 3 else "green"

    console.print(f"\n--- Password Analysis Report ---")
    console.print(f"Strength Score: [bold {color}]{score}/4[/bold {color}]")
    
    crack_time = results['crack_times_display']['offline_slow_hashing_1e4_per_second']
    console.print(f"Estimated time to crack: [bold]{crack_time}[/bold]")

    if results['feedback']['warning']:
        console.print(f"Warning: [yellow]{results['feedback']['warning']}[/yellow]")
    
    if results['feedback']['suggestions']:
        console.print("Suggestions:")
        for suggestion in results['feedback']['suggestions']:
            console.print(f"- {suggestion}")
    
    console.print("-" * 30)

def scan_passwords_from_file(file_path_str: str):
    """Scans passwords from a file and reports weaknesses."""
    file_path = Path(file_path_str)
    if not file_path.is_file():
        console.print(f"[bold red]Error: File not found at '{file_path}'[/bold red]")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except Exception as e:
        console.print(f"[bold red]Error reading file: {e}[/bold red]")
        return

    if not passwords:
        console.print("[yellow]The file is empty or contains no valid passwords.[/yellow]")
        return

    table = Table(title="Password Weakness Report")
    table.add_column("Password (Masked)", style="cyan")
    table.add_column("Strength (0-4)", justify="center")
    table.add_column("Weakness/Warning", style="yellow")
    table.add_column("Suggested Alternative", style="magenta")

    weak_passwords_found = 0
    for password in passwords:
        results = zxcvbn(password)
        score = results['score']

        if score < 3:
            weak_passwords_found += 1
            masked_pass = f"{password[0]}***{password[-1]}" if len(password) > 1 else "*"
            warning = results['feedback']['warning'] or "Uses common patterns."
            score_color = "red" if score < 2 else "yellow"
            score_display = f"[{score_color}]{score}[/{score_color}]"
            table.add_row(masked_pass, score_display, warning, generate_passphrase())
            
    if weak_passwords_found > 0:
        console.print(table)
    else:
        console.print("[bold green]✓ All passwords in the file appear to be strong![/bold green]")