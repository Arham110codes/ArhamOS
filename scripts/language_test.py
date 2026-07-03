from arhamos.tools.browser import BrowserService
from arhamos.tools.editor import LeetCodeEditor

browser = BrowserService()

browser.open("https://leetcode.com/problems/two-sum/")

input("Wait until the page loads, then press Enter...")

editor = LeetCodeEditor(browser.page)

print("Current Language:", editor.get_language())

editor.set_language("Java")

input("Verify Java is selected, then press Enter...")

browser.close()