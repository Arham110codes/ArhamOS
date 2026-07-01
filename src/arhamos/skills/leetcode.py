from rich.console import Console
from arhamos.core.llm import LLMClient

console = Console()


class LeetCodeSkill:
    def __init__(self):
        self.llm = LLMClient()

    def solve_problem(self):
        console.print("\n[bold cyan]LeetCode Learning Engine[/bold cyan]\n")

        problem = console.input(
            "[bold green]Paste the problem statement:[/bold green]\n\n"
        )

        console.print("\n[bold yellow]Thinking...[/bold yellow]\n")

        prompt = f"""
You are an expert competitive programmer.

Solve the following LeetCode problem.

Return:

1. Intuition
2. Brute Force Approach
3. Optimal Approach
4. Java Solution
5. Time Complexity
6. Space Complexity

Problem:

{problem}
"""

        response = self.llm.ask(prompt)

        console.print(response)