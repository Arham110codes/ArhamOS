from rich.console import Console

from arhamos.core.llm import LLMClient

console = Console()


class LeetCodeSkill:

    def __init__(self):
        self.llm = LLMClient()

    def solve_problem(self, problem: dict) -> str:

        console.print(
            f"\n[bold cyan]{problem['title']}[/bold cyan]"
        )

        console.print(
            f"[yellow]{problem['difficulty']}[/yellow]\n"
        )

        console.print(
            "[bold yellow]Thinking...[/bold yellow]\n"
        )

        prompt = f"""
You are an ICPC World Finalist and Senior Software Engineer.

Solve the following LeetCode problem.

Return ONLY the complete Java solution.

Do not include:
- Explanation
- Markdown
- Code fences
- Complexity analysis

Problem Title:
{problem["title"]}

Difficulty:
{problem["difficulty"]}

Problem Statement:
{problem["statement"]}
"""

        response = self.llm.ask(prompt)

        return response.strip()