import json
import os
from importlib import import_module
from importlib.resources import open_text

from src.fetcher import fetch
from src.notify import discordNotify


cwd = os.path.dirname(os.path.abspath(__file__))
with open(cwd + '/data/products.json', 'r') as products_fp:
    products = json.load(products_fp)

for (product, pinfo) in products.items():
    url = pinfo['URL']
    soup = fetch(url)
    store = import_module('src.stores.{}'.format(pinfo['store']))
    in_stock = store.inStock(soup)
    reminder_count = pinfo['reminder-counter']
    if in_stock != pinfo['in-stock'] or \
      (in_stock and reminder_count < 5):
        name = pinfo['name']
        message = "{} is now in stock!\n{}".format(name, url) if in_stock else \
                  "{} is now out of stock :sob:".format(name)
        discordNotify(os.environ[pinfo['channel-url']], message)
        products[product]['in-stock'] = in_stock
        products[product]['reminder-counter'] = reminder_count + 1 if in_stock else 0
        with open(cwd + '/data/products.json', 'w') as products_fp:
            json.dump(products, products_fp)
