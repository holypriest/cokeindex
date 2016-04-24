from decimal import Decimal

import requests
import json
from money import xrates

from config import CURRENCY_LAYER


DAILY_RATES_FILE = 'daily_rates.json'


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


def set_rates():

    xrates.install('money.exchange.SimpleBackend')
    xrates.base = 'USD'

    rates = read_daily_rates()

    # `quotes` is a dict in this format `"USDAAA": 42`, where AAA is the
    # target currency and 42 is the rate AAA / USD.
    quotes = rates['quotes']

    for key, value in quotes.iteritems():
        to_currency = key[3:]
        xrates.setrate(to_currency, Decimal(value))
