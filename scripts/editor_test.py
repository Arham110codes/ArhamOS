from arhamos.tools.browser import BrowserService
from arhamos.tools.editor import LeetCodeEditor

browser = BrowserService()

browser.open("https://leetcode.com/problems/two-sum/")

input("Open the editor if needed, then press Enter...")

editor = LeetCodeEditor(browser.page)

print(editor.detect())

input("Press Enter to exit...")