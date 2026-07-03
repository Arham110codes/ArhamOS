from arhamos.tools.browser import BrowserService
from arhamos.tools.leetcode_page import LeetCodePage
from arhamos.tools.editor import LeetCodeEditor

browser = BrowserService()

leetcode = LeetCodePage(browser.page)

leetcode.open_problem("https://leetcode.com/problems/two-sum/")

input("Open the coding editor manually once, then press Enter...")

leetcode.ensure_editor_open()

editor = LeetCodeEditor(browser.page)

java_code = """
class Solution {

    public int[] twoSum(int[] nums, int target) {
        return new int[]{0,1};
    }

}
"""

editor.set_code(java_code)

input("Press Enter to exit...")

browser.close()