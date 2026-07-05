from playwright.sync_api import Page


class ResultReader:

    def __init__(self, page: Page):
        self.page = page

    def click_run(self):

        self.page.get_by_role(
            "button",
            name="Run",
            exact=True,
        ).click()

        print("✓ Run clicked")

    def wait_for_completion(self):

        self.page.wait_for_load_state("networkidle")

        self.page.wait_for_timeout(3000)

        print("✓ Execution finished")