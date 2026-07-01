from playwright.sync_api import TimeoutError

from arhamos.tools.browser import BrowserService


class LeetCodeBrowser:
    def __init__(self):
        self.browser = BrowserService()

    def open_problem(self, slug: str):
        url = f"https://leetcode.com/problems/{slug}/"
        self.browser.open(url)

    def extract_problem(self):

        page = self.browser.page

        try:
            page.wait_for_selector('[data-track-load="description_content"]', timeout=10000)
        except TimeoutError:
            raise RuntimeError(
                "Could not load problem description. Are you logged in?"
            )

        title = page.locator('div.text-title-large a').inner_text()

        difficulty = page.locator(
            'div[class*="text-difficulty-"]'
        ).inner_text()

        statement = page.locator(
            '[data-track-load="description_content"]'
        ).inner_text()

        return {
            "title": title,
            "difficulty": difficulty,
            "statement": statement,
        }

    def close(self):
        self.browser.close()