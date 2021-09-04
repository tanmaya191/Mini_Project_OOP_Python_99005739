"""
Program to take input from CLI, it is not used here as the input is taken from GUI
language: Python 3
Designed By: Tanmaya Prasad Mangaraj
Email: tanmaya.mangaraj@ltts.com
PS ID: 99005739
Designation: Intern, L&T Technology Services
"""


def take_input():
    """take input from CLI"""
    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = float(input("Amount: "))
    return from_country, to_country, amount
