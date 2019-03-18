import requests
from bs4 import BeautifulSoup

url =  'https://www.filmweb.pl/films/search?orderBy=popularity&descending=true&page=1'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')


resultlist = soup.find('div', id='searchResult')
dict = []
for ele in resultlist.find_all('li', class_='hits__item'):
    #print(ele.prettify())

    original_title = ele.find('div', class_='filmPreview__originalTitle')
    if original_title is not None:
        original_title = original_title.text
    else:
        original_title = 'null'

    tmp = {
        'title': ele.find('h3', class_='filmPreview__title').text,
        'original_title': original_title,
        'year': ele.find('span', class_='filmPreview__year').text,
        'duration': ele.find('div', class_='filmPreview__filmTime')['data-duration'],

    }

    dict.append(tmp)
    print(tmp);