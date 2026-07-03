from arhamos.tools.browser import BrowserService

browser = BrowserService()

browser.open("https://leetcode.com/accounts/login/")

input(
    "\nIf you're not logged in, log in now.\n"
    "After reaching the LeetCode homepage, press ENTER..."
)

browser.close()