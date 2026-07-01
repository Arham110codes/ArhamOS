from rich.console import Console

from arhamos.workflows.base import Workflow

console = Console()


class LeetCodeWorkflow(Workflow):

    def setup(self):

        console.print("\n[bold cyan]Today's LeetCode Session[/bold cyan]\n")

        self.topic = console.input(
            "[green]Topic:[/green] "
        )

        self.count = int(
            console.input(
                "[green]Problems to solve:[/green] "
            )
        )

    def execute(self):

        console.print()

        console.print(f"Topic      : {self.topic}")

        console.print(f"Questions  : {self.count}")

        console.print("\nWorkflow initialized successfully.")

    def cleanup(self):

        console.print("\nSession complete.\n")