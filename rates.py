from config import CURRENCY_LAYER
import json

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
