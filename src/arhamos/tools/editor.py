from playwright.sync_api import Page


class LeetCodeEditor:

    def __init__(self, page: Page):
        self.page = page

    def detect(self):
        if self.page.locator(".monaco-editor").count() > 0:
            return "monaco"
        return None

    def set_code(self, code: str):

        editor = self.detect()

        if editor != "monaco":
            raise RuntimeError("Monaco editor not found.")

        self.page.evaluate(
            """
(code) => {
    monaco.editor.getModels()[0].setValue(code);
}
""",
            code,
        )

        print("✓ Code Injected")