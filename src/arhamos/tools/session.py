from arhamos.tools.browser import BrowserService


class SessionManager:

    def __init__(self):
        self.browser = BrowserService()

    def ensure_leetcode_login(self):

        self.browser.open("https://leetcode.com")

        page = self.browser.page

        page.wait_for_load_state("networkidle")

        if "login" in page.url.lower():

            print("\nPlease login to LeetCode.")
            print("Press ENTER after login is complete.\n")

            input()

            page.wait_for_load_state("networkidle")

        print("LeetCode session ready.")

        return page