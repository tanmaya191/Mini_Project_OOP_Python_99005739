"""
valid input checker using regular expressions
language: Python 3
Designed By: Tanmaya Prasad Mangaraj
Email: tanmaya.mangaraj@ltts.com
PS ID: 99005739
Designation: Intern, L&T Technology Services
"""
import re


def valid_input_check(k):
    """check weather the input is valid or not"""
    if re.match(r'^-?\d+(?:\.\d+)$', k) is None and re.match(r'[0-9]+$', k) is None:
        return False
    return True
