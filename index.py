#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import requests
import sys
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

reg_url = sys.argv[1]

req = requests.get(url=reg_url, headers=headers)

if req.status_code == 200:
    print('Requisição realizada sem erros')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')

divs = soup.find_all('div', {'class': ['lecture-container']})


def get_titles(lista):
    titulos = []
    for div in lista:
        id_video = div['data-purpose'].replace('lecture-item-', '')
        title = div.find("div", {"class": "title"}
                         ).get_text().replace('\n', '')
        duracao = div.find(
            "span", {"class": "content-summary"}).get_text().replace('\n', '')
        titulos.append(id_video + '.' + title + ' (' + duracao + ')')
    return titulos


with open('titulos.txt', 'w') as f:
    for titulo in get_titles(divs):
        f.write("%s\n" % titulo)
