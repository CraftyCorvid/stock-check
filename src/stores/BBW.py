from os import environ
from sys import exit as sys_exit
from src.notify import discordNotify

def inStock(soup):
    result = soup.find(class_='in-stock-msg')
    return not not result
