import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

from cli.menu import display_menu
from rich.console import Console

console = Console()


def main():

    while True:

        choice = display_menu()

        if choice == "1":
            console.print("\n[cyan]LeetCode Engine (Coming Next Step)[/cyan]")
            input("\nPress Enter to continue...")

        elif choice == "2":
            console.print("\n[cyan]Code Explainer (Coming Soon)[/cyan]")
            input("\nPress Enter to continue...")

        elif choice == "3":
            console.print("\nGoodbye Arham 👋")
            break

        else:
            console.print("\n[red]Invalid choice[/red]")
            input("\nPress Enter...")
            

if __name__ == "__main__":
    main()