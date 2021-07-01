import pytest
import json
import requests as re

# test exchange api
class TestCurrency:
    url = "https://api.exchangerate-api.com/v4/latest/USD"

# get request
    response = re.get(url).json()

    def test_basecurrency(self):
        self.basecurrency = self.response['base']
        assert self.basecurrency == 'KES'
    def test_date(self):
        self.date = self.response['date']
        assert self.date == "2021-06-30"
    def test_provider(self):
        self.provider = self.response['provider']
        assert self.provider == "https://www.exchangerate-api.com"
    def test_timelastupdated(self):
        self.timelastupdated = self.response['time_last_updated']
        assert self.timelastupdated == 1625011201  

