from arhamos.tools.browser import BrowserService


class LeetCodeBrowser:
    def __init__(self):
        self.browser = BrowserService()

    def open_problem(self, url: str):
        self.browser.open(url)

    def close(self):
        self.browser.close()