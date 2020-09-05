import requests
from sys import exit as sys_exit
from bs4 import BeautifulSoup

def fetch(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup
    except Exception as e:
        print(e)
        sys_exit()
