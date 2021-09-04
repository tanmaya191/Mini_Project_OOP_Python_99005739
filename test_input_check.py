"""
Test cases design to check valid_input_check function
language: Python 3
Designed By: Tanmaya Prasad Mangaraj
Email: tanmaya.mangaraj@ltts.com
PS ID: 99005739
Designation: Intern, L&T Technology Services
"""

from input_check import valid_input_check


def test_integer_inputs():
    """integer input check"""
    assert True is valid_input_check('6')
    assert True is valid_input_check('4555')
    assert True is valid_input_check('35')
    assert True is valid_input_check('865')


def test_floating_inputs():
    """floating input check"""
    assert True is valid_input_check('6.5')
    assert True is valid_input_check('0.64')
    assert True is valid_input_check('6942.25')
    assert True is valid_input_check('529.625')


def test_string_inputs():
    """string input check"""
    assert False is valid_input_check('hi')
    assert False is valid_input_check('hfesf')
    assert False is valid_input_check('gzFEFG')
    assert False is valid_input_check('GrtghG')


def test_string_integer_inputs():
    """string+ integer input check"""
    assert False is valid_input_check('GGEhh62f')
    assert False is valid_input_check('JGYH369jde')
    assert False is valid_input_check('5603hjwkJG')
    assert False is valid_input_check('wjeb65')


def test_special_character_inputs():
    """special character check"""
    assert False is valid_input_check('@')
    assert False is valid_input_check('852#')
    assert False is valid_input_check('$##fd%')
    assert False is valid_input_check('$#DF23')
