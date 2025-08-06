import os
import time
from rich.console import Console

# Import the core functions from our other file
from password_analyzer_core import (
    analyze_password_strength,
    generate_passphrase,
    generate_random_password,
    scan_passwords_from_file
)

console = Console()

# --- ASCII Art Banners (UPDATED) ---
PASSWORD_BANNER = """
██████╗  █████╗ ███████╗███████╗██████╗  ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██████╔╝██║   ██║██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║██╔══██╗██║   ██║██╔═══╝ 
██║     ██║  ██║███████║███████║██████╔╝╚██████╔╝██║     
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚═╝     
"""

ANALYZER_TOOL_BANNER = """
 █████╗ ███╗   ██╗ █████╗ ██╗     ███████╗███████╗   ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗████╗  ██║██╔══██╗██║     ██╔════╝██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
███████║██╔██╗ ██║███████║██║     ███████╗███████╗      ██║   ██║   ██║██║   ██║██║     
██╔══██║██║╚██╗██║██╔══██║██║     ╚════██║╚════██║      ██║   ██║   ██║██║   ██║██║     
██║  ██║██║ ╚████║██║  ██║███████╗███████║███████║      ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
"""


# --- Helper Functions for the UI ---

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    """Displays the main header and creator info."""
    clear_screen()
    # Print the new banners
    console.print(f"[bold orange1]{PASSWORD_BANNER}[/bold orange1]")
    console.print(f"[bold yellow]{ANALYZER_TOOL_BANNER}[/bold yellow]")
    console.print("[bold cyan]Coded By: Amol Waditke[/bold cyan]", justify="center")
    console.print("[red]This Tool is Only For Educational Purposes. Please Don't use for Any Illegal Activity.[/red]\n")

def display_menu():
    """Displays the main menu options."""
    console.print("[bold green][01] Analyze a Single Password[/bold green]")
    console.print("[bold green][02] Generate a Strong Password[/bold green]")
    console.print("[bold green][03] Scan Passwords From a File[/bold green]")
    console.print("[bold red][99] Exit[/bold red]\n")


# --- Main Application Logic ---

def main():
    while True:
        display_header()
        display_menu()
        
        try:
            choice = console.input("[bold magenta]AmolWaditke --> [/bold magenta]")

            if choice == '1':
                password = console.input("[yellow]Enter the password to analyze: [/yellow]")
                analyze_password_strength(password)
            
            elif choice == '2':
                console.print("[cyan]Choose password type:[/cyan]")
                console.print("[cyan]  1. Memorable Passphrase (e.g., apple-rocket-winter)[/cyan]")
                console.print("[cyan]  2. Random Character String (e.g., a@!#T5^gE)[/cyan]")
                gen_choice = console.input("[yellow]Enter choice (1/2): [/yellow]")
                if gen_choice == '1':
                    new_pass = generate_passphrase()
                    console.print(f"\n[bold green]Generated Passphrase: {new_pass}[/bold green]")
                elif gen_choice == '2':
                    try:
                        length = int(console.input("[yellow]Enter desired length (e.g., 16): [/yellow]"))
                        new_pass = generate_random_password(length)
                        console.print(f"\n[bold green]Generated Password: {new_pass}[/bold green]")
                    except ValueError:
                        console.print("[bold red]Invalid length. Please enter a number.[/bold red]")
                else:
                    console.print("[bold red]Invalid choice.[/bold red]")

            elif choice == '3':
                file_path = console.input("[yellow]Enter the full path to the password file: [/yellow]")
                scan_passwords_from_file(file_path)

            elif choice == '99':
                console.print("[bold yellow]Exiting tool. Stay safe![/bold yellow]")
                break
            
            else:
                console.print("[bold red]Invalid option, please try again.[/bold red]")
            
            # Pause to allow user to read output before clearing screen
            console.input("\n[cyan]Press Enter to return to the main menu...[/cyan]")

        except KeyboardInterrupt:
            console.print("\n[bold yellow]Exiting tool. Stay safe![/bold yellow]")
            break

if __name__ == "__main__":
    main()