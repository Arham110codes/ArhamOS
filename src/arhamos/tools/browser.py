from playwright.sync_api import sync_playwright


class BrowserService:

    def __init__(self):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.connect_over_cdp(
            "http://127.0.0.1:9222"
        )

        if not self.browser.contexts:
            raise RuntimeError("No browser context found.")

        self.context = self.browser.contexts[0]

        # Find the first usable page
        self.page = None

        for page in self.context.pages:
            try:
                _ = page.title()
                self.page = page
                break
            except Exception:
                continue

        if self.page is None:
            self.page = self.context.new_page()

    def open(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def close(self):
        # Disconnect only. Keep Edge running.
        self.browser.close()
        self.playwright.stop()