from rich.console import Console

from arhamos.cli.menu import display_menu
from arhamos.workflows.leetcode import LeetCodeWorkflow

console = Console()


def main():
    while True:
        choice = display_menu()

        if choice == "1":
            LeetCodeWorkflow().run()
            input("\nPress Enter to continue...")

        elif choice == "2":
            console.print("\n[cyan]Code Explainer (Coming Soon)[/cyan]")
            input("\nPress Enter to continue...")

        elif choice == "3":
            console.print("\n[green]Goodbye Arham 👋[/green]")
            break

        else:
            console.print("\n[red]Invalid choice[/red]")
            input("\nPress Enter...")


if __name__ == "__main__":
    main()