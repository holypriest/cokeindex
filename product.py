from money import Money
import requests
from bs4 import BeautifulSoup
import re
from rates import *

class Product(object):

    def __init__(self, seller, selector, url):
        self.seller = seller
        self.selector = selector
        self.url = url
        self._price = self.get_price()

    @property
    def price(self):
        return self._price

    def fetch(self, url):
        r = requests.get(url)
        return r.text

    def get_price_str(self, text, selector):
        soup = BeautifulSoup(text, 'html.parser')
        result = soup.select(selector)
        return result[0].text

    def fix_price(self, price_str):
        price = re.sub(r',', '.', price_str)
        return float(re.sub(r'[^0-9\.]', '', price))

    def get_price(self):
        price_str = self.get_price_str(self.fetch(self.url), self.selector)
        price = self.fix_price(price_str)
        country = self.seller.country
        currency = country.currency
        m = Money(amount=price, currency=currency)
        return m

    def get_usd_price(self, rates):
        rate = rates['quotes']['USD' + self._price.currency]
        usd_price = float(self.price.amount) / rate
        return Money(amount=usd_price, currency='USD')
