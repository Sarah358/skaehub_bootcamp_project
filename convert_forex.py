from unittest import result
from forex_python.converter import CurrencyCodes, CurrencyRates
from forex_python.bitcoin import BtcConverter

# test = CurrencyCodes()
test = CurrencyCodes()
c = CurrencyRates()
b = BtcConverter() 

def get_name(cur_name):
    return test.get_currency_name(cur_name)

# get currency symbol

def get_symbol(cur_symbol):
    return test.get_symbol(cur_symbol)

# convert bitcoin to currency
def get_cur(amount,currency):
    return b.convert_btc_to_cur(amount,currency)

# converting amounts
def conversion(from_currency,to_currency,amount):
    return c.convert(from_currency, to_currency, amount)

# print(result)

