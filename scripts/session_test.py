from arhamos.tools.session import SessionManager

session = SessionManager()

session.ensure_leetcode_login()

input("\nPress Enter to close...")

session.browser.close()