from pprint import pprint

from arhamos.tools.leetcode import LeetCodeBrowser

lc = LeetCodeBrowser()

lc.open_problem("two-sum")

problem = lc.extract_problem()

pprint(problem)

input("\nPress Enter...")

lc.close()