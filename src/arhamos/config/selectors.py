"""
Centralized DOM selectors used throughout ArhamOS.

If LeetCode updates its UI, this should be the only file
requiring changes.
"""


# --------------------------
# Editor
# --------------------------

MONACO_EDITOR = ".monaco-editor"

CODEMIRROR_EDITOR = ".cm-editor"


# --------------------------
# Language
# --------------------------

LANGUAGE_BUTTON = 'button[aria-haspopup="dialog"]'

LANGUAGE_MENU = '[role="dialog"]'

JAVA_OPTION = 'text=Java'


# --------------------------
# Problem
# --------------------------

PROBLEM_TITLE = 'div.text-title-large'

PROBLEM_DESCRIPTION = '[data-track-load="description_content"]'


# --------------------------
# Run
# --------------------------

RUN_BUTTON = 'button:has-text("Run")'

RUN_RESULT = '[data-e2e-locator="console-result"]'


# --------------------------
# Submit
# --------------------------

SUBMIT_BUTTON = 'button:has-text("Submit")'

SUBMISSION_RESULT = '[data-e2e-locator="submission-result"]'


# --------------------------
# Monaco
# --------------------------

MONACO_VIEW = ".view-lines"