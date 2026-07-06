from playwright.sync_api import Page

from arhamos.config import selectors


class LeetCodeEditor:

    def __init__(self, page: Page):
        self.page = page

    def detect(self):

        if self.page.locator(selectors.MONACO_EDITOR).count() > 0:
            return "monaco"

        if self.page.locator(selectors.CODEMIRROR_EDITOR).count() > 0:
            return "codemirror"

        return None

    def get_language(self) -> str:

     button = self.page.locator('button[aria-haspopup="dialog"]').nth(1)

     return button.inner_text().replace("▼", "").strip()

    def set_language(self, language: str):

        current = self.get_language()

        if current == language:
            print(f"✓ Language already {language}")
            return
        # Click the language button (index 1)
        self.page.locator('button[aria-haspopup="dialog"]').nth(1).click()

        # Wait for popup
        self.page.locator('[role="dialog"]').wait_for(state="visible")

        # Click Java inside popup
        self.page.locator('[role="dialog"] div.text-sm').filter(
            has_text=language
        ).first.click()

        self.page.wait_for_timeout(500)
        new_language = self.get_language()

        if new_language != language:
            raise RuntimeError(
                f"Failed to switch language to {language}"
            )

        print(f"✓ Language switched to {language}")

    def set_code(self, code: str):

        editor = self.detect()

        if editor != "monaco":
            raise RuntimeError("Monaco editor not found.")

        self.set_language("Java")

        self.page.evaluate(
            """
(code) => {
    monaco.editor.getModels()[0].setValue(code);
}
""",
            code,
        )

        print("✓ Code Injected")