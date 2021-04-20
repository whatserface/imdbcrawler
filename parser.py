import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import re
from collections import Counter
import pandas as pd
def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'upgrade-insecure-requests': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'referer': 'https://www.google.com/',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive'
        }
    req = requests.get(url, headers=headers)
    bs_obj = bs(req.content, features='lxml')
    return bs_obj
soup = get_data('https://www.imdb.com/chart/top/')
i = 0
links = soup.select("tbody.lister-list tr td.titleColumn a")
countries, years, genres = [], [], []
def get_info(soup):
    global countries, years, genres
    year = soup.find('span', id='titleYear').text[1:-1]
    genre = soup.select("div.subtext a:not([title])")
    country = soup.find_all('h4', class_='inline', string='Country:')[0].find_parent().text
    country = re.sub(r'(\n\|\n|\n)', ',', country)
    country = ''.join(re.compile(r'(\w|:|,)').findall(country, 10, len(country)-1)).split(',')
    countries += country
    years.append(year)
    genres += [i.text for i in genre]
for link in links:
    i += 1
    print(i)
    get_info(get_data("https://www.imdb.com/" + str(link['href'])))
top = 5
c_countries = Counter(countries)
c_years = Counter(years)
c_genres = Counter(genres)
data = {'countries': c_countries.most_common(top), 'years': c_years.most_common(top), 'genres': c_genres.most_common(top)}
pprint(data)
df = pd.DataFrame(data, index=range(1, top+1))
df.to_excel('report.xlsx')