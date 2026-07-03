from arhamos.tools.leetcode import LeetCodeBrowser
from arhamos.skills.leetcode import LeetCodeSkill

browser = LeetCodeBrowser()

browser.open_problem("two-sum")

problem = browser.extract_problem()

LeetCodeSkill().solve_problem(problem)

input("\nPress Enter...")

browser.close()