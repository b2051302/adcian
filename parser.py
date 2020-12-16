# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv

CSV = 'tap.csv'
URL = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&region=1&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1'
HEADERS = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

def get_html(url,params=''):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('div',class_='_93444fe79c--wrapper--E9jWb').find_all('article', class_ = '_93444fe79c--container--2pFUD _93444fe79c--cont--1Ddh2')
    tap = []

    for item in content:
        try:
            tap.append(
            {

                    'title':item.find('div', class_='_93444fe79c--container--JdWD4').get_text(strip = True),
                    'price':item.find('span', class_ ='_93444fe79c--color_black_100--A_xYw _93444fe79c--lineHeight_28px--3QLml _93444fe79c--fontWeight_bold--t3Ars _93444fe79c--fontSize_22px--3UVPd _93444fe79c--display_block--1eYsq _93444fe79c--text--2_SER').get_text(strip = True),
                    'link':item.find('div', class_ = '_93444fe79c--container--2Kouc _93444fe79c--link--2-ANY').find('a').get('href'),
                    'img':item.find('div', class_ = '_93444fe79c--container--3FC45 _93444fe79c--container--2sKn2').find('img').get('src'),

            }
            )
        except:
            continue;
    return tap

def save_doc(items, path):
    with open(path, 'w', newline = '', encoding='utf8') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['Название объявления', 'Цена', 'Ссылка', 'Изображение'])
        for item in items:
            writer.writerow([item['title'], item['price'], item['link'], item['img']])

def parser():
    PAGENATION = input('Укажите количество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        tap = []
        for page in range(1, PAGENATION+1):
            print(f'Парсим страницу: {page}')
            html = get_html(URL, params = {'p': page})
            tap.extend(get_content(html.text))
            save_doc(tap, CSV)
        print('Парсинг закончен')
    else:
        print('Error')


parser()