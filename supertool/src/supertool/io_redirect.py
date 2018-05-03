"""
This module contains context managers for redirecting input and output for some code.
"""

import sys
import io


class StdInRedirector:
    """
    Instances of this class are used as context managers which temporary redirect input that some code requires into a
    StringIO object.
    """
    def __init__(self, args):
        self.args = args

    def __enter__(self):
        sys.stdin = io.StringIO(self.args)

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdin = sys.__stdin__


class StdOutRedirector:
    """
    Instances of this class are used as context managers which temporary redirect the output of the code into a StringIO
    object.
    """
    def __enter__(self):
        self.oldstdout = sys.stdout
        sys.stdout = io.StringIO()

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.oldstdout
