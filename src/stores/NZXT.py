from os import environ
from sys import exit as sys_exit
from src.notify import discordNotify

def inStock(soup):
    try:
        result = soup.find(class_='add-to-cart-btn').button.string
    except AttributeError as e:
        discordNotify(environ['ERRORS_WEBHOOK'], 'NZXT: Unexpected HTML!\n{}'.format(e))
        sys_exit()
    return (result != "Sold Out")
