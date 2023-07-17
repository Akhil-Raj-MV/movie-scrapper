import urllib.request as UrlReq
import sys
from bs4 import BeautifulSoup
from tqdm import tqdm

name = input('Enter your name of the file: ')
year = str(int(input('Enter the year : ')))

sys.stdout = open(name + '_IMDB_Top_50_FOR' + year + '.txt', 'w')

url = "http://www.imdb.com/search/title?release_date=" + year + "," + year + "&title_type=feature"
ourUrl=UrlReq.urlopen(url).read()
soup = BeautifulSoup(ourUrl,features="lxml")

article = soup.find('div', attrs={'class': 'article'}).find('h1')
print(article.contents[0] + ': ')

lister_list_contents = soup.find('div', attrs={'class': 'lister-list'})
i = 1
movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})

for movie in tqdm(movieList):
    print(str(i) + '.'),
    header = movie.findChildren('h3', attrs={'class': 'lister-item-header'})

    for items in header:
        title = header[0].findChildren('a')
        print('Movie: ' + str(title[0].contents[0]))
    
    genre = movie.findChildren('span', attrs={'class': 'genre'})
    print('Genre: ' + genre[0].text.encode('utf-8').decode('ascii', 'ignore'))

    description = movie.findChildren('p', attrs={'class': 'text-muted'})
    description_text = description[0].text.encode('utf-8').decode('ascii', 'ignore')
    print('Description: ' + description_text)
    
    i += 1