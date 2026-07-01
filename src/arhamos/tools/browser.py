from playwright.sync_api import sync_playwright


class BrowserService:
    def __init__(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch_persistent_context(
            user_data_dir="user_data",
            headless=False,
        )

        self.page = self.browser.new_page()

    def open(self, url: str):
        self.page.goto(url)

    def close(self):
        self.browser.close()
        self.playwright.stop()