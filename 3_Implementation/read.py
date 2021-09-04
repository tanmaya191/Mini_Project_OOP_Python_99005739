"""
program to read currency rate text file
language: Python 3
Designed By: Tanmaya Prasad Mangaraj
Email: tanmaya.mangaraj@ltts.com
PS ID: 99005739
Designation: Intern, L&T Technology Services
"""

# importing the library
import ast


def read_rates_file():
    """reading the data from the file"""
    with open('currency_rates.txt', encoding='utf8') as curr_file:
        data = curr_file.read()

    #print("Data type before reconstruction : ", type(data))

    # reconstructing the data as a dictionary
    curr_data = ast.literal_eval(data)

    #print("Data type after reconstruction : ", type(d))

    return curr_data
