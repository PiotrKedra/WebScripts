import json

import requests
from bs4 import BeautifulSoup

url =  'https://www.filmweb.pl/films/search?orderBy=popularity&descending=true&page=1'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')


resultlist = soup.find('div', id='searchResult')
dict = []
for ele in resultlist.find_all('li', class_='hits__item'):

    original_title = ele.find('div', class_='filmPreview__originalTitle')
    if original_title is not None:
        original_title = original_title.text
    else:
        original_title = 'null'

    gatunek = ele.find('div', class_='filmPreview__info filmPreview__info--genres').find_all('li')
    genres = []
    for gen in gatunek:
        genres.append(gen.text)

    from_where = ele.find('div', class_='filmPreview__info filmPreview__info--countries').find_all('li')
    countries = []
    for countrie in from_where:
        countries.append(countrie.text)

    directors_result = ele.find('div', class_='filmPreview__info filmPreview__info--directors').find_all('li')
    directors = []
    for director in directors_result:
        directors.append(director.text)


    cast_result = ele.find('div', class_='filmPreview__info filmPreview__info--cast')
    cast = []
    if cast_result is not None:
        cast_result = cast_result.find_all('li')
        for actor in cast_result:
            cast.append(actor.text)



    tmp = {
        'title': ele.find('h3', class_='filmPreview__title').text,
        'original_title': original_title,
        'year': ele.find('span', class_='filmPreview__year').text,
        'duration': ele.find('div', class_='filmPreview__filmTime')['data-duration'],
        'rate': ele.find('span', class_='rateBox__rate').text,
        'rate_votes': ele.find('div', class_='filmPreview__rateBox rateBox')['data-count'],
        'description': ele.find('div', class_='filmPreview__description').text,
        'genres': genres,
        'countries': countries,
        'directors': directors,
        'cast': cast,
        'movie_img_url': ele.find('div', class_='filmPoster__imageWrap').find('img')['data-src'],
        'movie_trailer_url': 'https://www.filmweb.pl' + ele.find('a', class_='filmPoster__videoLink')['href']


    }

    dict.append(tmp)
    #print(tmp);

with open('data.json', 'w') as outfile:
    json.dump(dict, outfile, indent = True, ensure_ascii=False)