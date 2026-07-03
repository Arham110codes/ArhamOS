from playwright.sync_api import Page


class LeetCodePage:

    def __init__(self, page: Page):
        self.page = page

    def open_problem(self, url: str):

        self.page.goto(url, wait_until="domcontentloaded")

    def ensure_editor_open(self):

        # Wait until the editor container exists
        self.page.wait_for_selector(".monaco-editor", timeout=30000)

        print("✓ Editor Ready")