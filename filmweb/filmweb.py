import json

import requests
from bs4 import BeautifulSoup

"""
It generate json file with almost 10 000 movies from filmweb. One json record looks like:
{
    'title': title,
    'original_title': original_title,
    'year': year,
    'duration': duration,
    'rate': rate,
    'rate_votes': rate_votes,
    'description': description,
    'genres': genres [],
    'countries': countries [],
    'directors': directors [],
    'cast': cast [],
    'movie_img_url': movie_img,
    'movie_trailer_url': trailer,
}

if some record is null he has value of 'null', if it is a list[], it is a list[] with 0 elements
"""

file_name = 'new_file_name'

movie_list = []
for i in range(1, 1001):

    print(i)

    url = f'https://www.filmweb.pl/films/search?orderBy=popularity&descending=true&page={i}'
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')

    result_movie_list = soup.find('div', id='searchResult')
    for ele in result_movie_list.find_all('li', class_='hits__item'):

        title = ele.find('h3', class_='filmPreview__title')
        if title is not None:
            title = title.text
        else:
            continue

        year = ele.find('span', class_='filmPreview__year')
        if year is not None:
            year = year.text
            if int(year) > 2019:
                continue
        else:
            continue

        original_title = ele.find('div', class_='filmPreview__originalTitle')
        if original_title is not None:
            original_title = original_title.text
        else:
            original_title = 'null'

        genres_set = ele.find('div', class_='filmPreview__info filmPreview__info--genres')
        genres = []
        if genres_set is not None:
            genres_set = genres_set.find_all('li')
            for gen in genres_set:
                genres.append(gen.text)

        from_where = ele.find('div', class_='filmPreview__info filmPreview__info--countries')
        countries = []
        if from_where is not None:
            from_where = from_where.find_all('li')
            for country in from_where:
                countries.append(country.text)

        directors_result = ele.find('div', class_='filmPreview__info filmPreview__info--directors')
        directors = []
        if directors_result is not None:
            directors_result = directors_result.find_all('li')
            for director in directors_result:
                directors.append(director.text)

        cast_result = ele.find('div', class_='filmPreview__info filmPreview__info--cast')
        cast = []
        if cast_result is not None:
            cast_result = cast_result.find_all('li')
            for actor in cast_result:
                cast.append(actor.text)

        trailer = ele.find('a', class_='filmPoster__videoLink')
        if trailer is not None:
            trailer = 'https://www.filmweb.pl' + trailer['href']
        else:
            trailer = 'null'

        duration = ele.find('div', class_='filmPreview__filmTime')
        if duration is not None:
            duration = duration['data-duration']
        else:
            duration = 'null'

        # If there is no rate move probably wasn't recorded so we skip it
        rate = ele.find('span', class_='rateBox__rate')
        if rate is not None:
            rate = rate.text
        else:
            rate = 'null'
            continue

        rate_votes = ele.find('div', class_='filmPreview__rateBox rateBox')
        if rate_votes is not None:
            rate_votes = rate_votes['data-count']
        else:
            rate_votes = 'null'

        description = ele.find('div', class_='filmPreview__description')
        if description is not None:
            description = description.text
        else:
            description = 'null'

        movie_img = ele.find('div', class_='filmPoster__imageWrap')
        if movie_img is not None:
            movie_img = movie_img.find('img')
            if movie_img is not None:
                movie_img = movie_img['data-src']
            else:
                movie_img = 'null'
        else:
            movie_img = 'null'

        movie_dict = {
            'title': title,
            'original_title': original_title,
            'year': year,
            'duration': duration,
            'rate': rate,
            'rate_votes': rate_votes,
            'description': description,
            'genres': genres,
            'countries': countries,
            'directors': directors,
            'cast': cast,
            'movie_img_url': movie_img,
            'movie_trailer_url': trailer,
        }

        movie_list.append(movie_dict)


with open(file_name, 'w', encoding='utf-8') as outfile:
    json.dump(movie_list, outfile, indent=True, ensure_ascii=False)

print('movies: ')
print(len(movie_list))
