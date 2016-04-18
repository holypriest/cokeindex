#!/usr/bin/env python
# -*- coding: utf-8 -*-

from seller import Seller
from product import Product
from country import Country
from rates import *

data = {
    'pda' : {
        'selector': '#productForm > div.product-control__price.product-control__container > span.value.inline--middle',
        'url': 'http://www.paodeacucar.com.br/produto/116609',
        'country': 'Brazil',
        'currency': 'BRL',
    },
    'extra' : {
        'selector': '#prod_116609 > p',
        'url': 'http://www.deliveryextra.com.br/produto/116609/refrigerante-coca-cola-lata-350ml',
        'country': 'Brazil',
        'currency': 'BRL',
    },
    'ardis': {
        'selector': '#main_container > section > div > div.span5 > div > div.price_block.line-dashed > p > span',
        'url': 'http://www.ardis.dz/arproduit_detail.php?Id_Prod=10000086',
        'country': 'Algeria',
        'currency': 'DZD',
    },
    'tesco': {
        'selector': '#yui_3_13_0_1_1460938557136_343 > div.quantityWrapper > div > p.price > span.linePrice',
        'url': 'http://www.tesco.com/groceries/product/details/?id=254855716',
        'country': 'England',
        'currency': 'GBP',
    },
}

def main():

    rates = read_daily_rates()

    for key in data:
        c = Country(data[key]['country'], data[key]['currency'])
        s = Seller(key, c)
        p = Product(s, data[key]['selector'], data[key]['url'])
        print("%s\t\t\t%s" % (s.name.upper(), p.get_usd_price(rates)))

if __name__ == '__main__':
    main()
