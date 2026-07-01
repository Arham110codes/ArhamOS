from rich.console import Console
from rich.panel import Panel

console = Console()


def display_menu():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]ArhamOS[/bold cyan]\n"
            "AI Engineering Platform",
            border_style="cyan",
        )
    )

    console.print()

    console.print("[1] LeetCode Learning Engine")
    console.print("[2] Code Explainer")
    console.print("[3] Exit")

    console.print()

    return console.input("[bold green]> [/bold green]")