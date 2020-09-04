import requests
from bs4 import BeautifulSoup
from discordwebhook import Discord
from os import environ

URL = 'https://www.nzxt.com/products/h1-matte-black'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find(class_='add-to-cart-btn').button.string
discord = Discord(url=environ['DISCORD_WEBHOOK_URL'])

if result != "Sold Out":
    discord.post(content="NZXT H1 is in-stock!\nhttps://www.nzxt.com/products/h1-matte-black")
