#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
from money import Money
from config import CURRENCY_LAYER
import json

data = {
    'pda' : {
        'selector': '#productForm > div.product-control__price.product-control__container > span.value.inline--middle',
        'url': 'http://www.paodeacucar.com.br/produto/116609',
        'country': 'brazil',
        'currency': 'BRL',
    },
    'extra' : {
        'selector': '#prod_116609 > p',
        'url': 'http://www.deliveryextra.com.br/produto/116609/refrigerante-coca-cola-lata-350ml',
        'country': 'brazil',
        'currency': 'BRL',
    },
    'ardis': {
        'selector': '#main_container > section > div > div.span5 > div > div.price_block.line-dashed > p > span',
        'url': 'http://www.ardis.dz/arproduit_detail.php?Id_Prod=10000086',
        'country': 'Algeria',
        'currency': 'DZD',
    },
}

DAILY_RATES_FILE = 'daily_rates.json'

def main():

    for key in data:
        print("%s\t\t\t%s" % (key.upper(), show_me_the_money(key)))

def fetch(url):

    r = requests.get(url)
    return r.text

def get_price(text, selector):

    soup = BeautifulSoup(text, 'html.parser')
    result = soup.select(selector)

    return float(fix_price(result[0].text))

def get_data(key):
    return (data[key]['selector'], data[key]['url'])

def fix_price(price_str):
    price = re.sub(r',', '.', price_str)
    return float(re.sub(r'[^0-9\.]', '', price))

def show_me_the_money(key):
    selector, url = get_data(key)
    price = get_price(fetch(url), selector)
    currency = data[key]['currency']
    m = Money(amount=price, currency=currency)
    return m

def get_all_rates():
    params= {
        'access_key': CURRENCY_LAYER,
        'format': 1,
    }

    r = requests.get("http://apilayer.net/api/live", params=params)
    with open(DAILY_RATES_FILE,'w') as f:
        f.write(r.text)

def read_daily_rates():
    with open(DAILY_RATES_FILE,'r') as f:
         text = f.read()

    return json.loads(text)

if __name__ == '__main__':
    main()
