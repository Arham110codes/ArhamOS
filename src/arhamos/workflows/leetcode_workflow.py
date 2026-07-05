from rich.console import Console

from arhamos.tools.browser import BrowserService
from arhamos.tools.leetcode_page import LeetCodePage
from arhamos.tools.editor import LeetCodeEditor
from arhamos.skills.leetcode import LeetCodeSkill
from arhamos.tools.result import ResultReader

console = Console()


class LeetCodeWorkflow:

    def run(self):

        browser = BrowserService()

        leetcode = LeetCodePage(browser.page)

        editor = LeetCodeEditor(browser.page)

        skill = LeetCodeSkill()

        console.print("[green]Connected to browser.[/green]")

        # leetcode.open_problem("https://leetcode.com/problems/two-sum/")

        # input(
        #     "\nOpen the coding editor if needed, then press Enter..."
        # )
        console.print("[green]Using currently open LeetCode page.[/green]")

        problem = {
            "title": "Two Sum",
            "difficulty": "Easy",
            "statement": browser.page.locator(
                '[data-track-load="description_content"]'
            ).inner_text(),
        }

        solution = skill.solve_problem(problem)

        console.print("\n[yellow]Injecting solution...[/yellow]")

        editor.set_code(solution)
        result = ResultReader(browser.page)

        console.print(
            "\n[yellow]Running solution...[/yellow]"
        )

        result.click_run()

        result.wait_for_completion()

        console.print(
            "\n[green]Done. Review the solution before submitting.[/green]"
        )

        input("\nPress Enter to disconnect...")

        browser.close()