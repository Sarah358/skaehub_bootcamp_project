import unittest
from unittest import result
import convert_forex

class TestCurrencies(unittest.TestCase):
    # test function
    # test currency name
    def test_cur_name(self):
        a = 'KES' 
        result = convert_forex.get_name(a)
        self.assertEqual(result,'Kenyan Shilling')
        # test currency symbol
    def test_symbol(self):
        b = 'USD'
        result = convert_forex.get_symbol(b)
        self.assertEqual(result,'$')
    # test converting bitcoin to currency
    def test_get_currency(self):
        bit = 1
        cur = 'KES'
        result = convert_forex.get_cur(bit,cur)
        self.assertEqual(result,258)
    # test for real time currency conversion
    def test_conversion(self):
        currency_from = 'USD'
        currency_to = 'KES'
        amount = 20
        result = convert_forex.conversion(currency_from,currency_to,amount)
        self.assertEqual(result,1254)

   

if __name__ == '__main__':
    unittest.main()