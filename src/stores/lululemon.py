from os import environ
from sys import exit as sys_exit
from src.notify import discordNotify

def inStock(soup):
    result = soup.find(id='purchase-attributes-size-notification-error').div.string
    return (result != "Sold out online.")
