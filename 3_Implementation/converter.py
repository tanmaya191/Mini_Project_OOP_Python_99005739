"""
program to convert the currency of one country to that of another country
language: Python 3
Designed By: Tanmaya Prasad Mangaraj
Email: tanmaya.mangaraj@ltts.com
PS ID: 99005739
Designation: Intern, L&T Technology Services
"""

# Import the modules needed
import requests


class CurrencyConvertor:
    """Class currencu converter to convert currency from one to another"""

    # empty dict
    rates = {}

    def __init__(self, url):
        """fetch data from url and store it in a text file"""
        data = requests.get(url).json()

        # Extracting only the rates from the json data
        self.rates = data["rates"]

        try:
            geeky_file = open('currency_rates.txt', 'wt', encoding='utf8')
            geeky_file.write(str(self.rates))
            geeky_file.close()

        except:
            print("Unable to write to file")

    def convert(self, from_currency, to_currency, amount_for_conversion):
        """currency conversion"""
        initial_amount = amount_for_conversion
        if from_currency != 'EUR':
            amount_for_conversion = amount_for_conversion / self.rates[from_currency]

        # limiting the precision to 2 decimal places
        amount_for_conversion = round(amount_for_conversion * self.rates[to_currency], 4)

        print('{} {} = '.format(initial_amount, from_currency, ), end="")
        print('{} {} '.format(amount_for_conversion, to_currency))
        return str(amount_for_conversion)
