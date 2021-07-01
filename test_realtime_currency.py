import unittest
from unittest import result
import realtime_currency
import json
import requests

class TestCurrencies(unittest.TestCase):
    # test function
    def test_convert(self,amount):
        amount = 0.587545
        result = realtime_currency.RealTimeCurrencyConverter.convert(round(amount),4)
        self.assertEqual(result,0.5875)

if __name__ == '__main__':
    unittest.main()



