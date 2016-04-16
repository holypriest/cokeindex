#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

data = {
    'pda' : {
        'selector': '#productForm > div.product-control__price.product-control__container > span.value.inline--middle',
        'url': 'http://www.paodeacucar.com.br/produto/116609',
        'country': 'brazil',
    },
    'extra' : {
        'selector': '#prod_116609 > p',
        'url': 'http://www.deliveryextra.com.br/produto/116609/refrigerante-coca-cola-lata-350ml',
        'country': 'brazil',
    },
    'ardis': {
        'selector': '#main_container > section:nth-child(2) > div > div.span5 > div > div.price_block.line-dashed > p:nth-child(2) > span',
        'url': 'http://www.ardis.dz/arproduit_detail.php?Id_Prod=10000086',
        'country': 'algeria',
    },
}

def main():

    selector, url = get_data('extra')

    content = fetch(url)
    price = get_price(content, selector)

    print(price)

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


if __name__ == '__main__':
    main()
