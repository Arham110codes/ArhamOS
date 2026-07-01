import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

from rich.console import Console
from core.llm import LLMClient

console = Console()


def banner():
    console.rule("[bold cyan]ArhamOS v0.1[/bold cyan]")


def main():
    banner()

    console.print("[green]✓ Configuration Loaded[/green]")
    console.print("[green]✓ Ollama Connected[/green]\n")

    llm = LLMClient()

    response = llm.ask(
        "Introduce yourself to Arham in exactly two sentences."
    )

    console.print(response)


if __name__ == "__main__":
    main()