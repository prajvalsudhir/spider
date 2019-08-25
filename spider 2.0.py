import requests
from bs4 import BeautifulSoup

def spider(pages):
    page=1
    while page<=pages:
        url='https://seattle.craigslist.org/search/jjj'
        source=requests.get(url)
        text=source.text
        soup=BeautifulSoup(text,'html.parser')
        for link in soup.findAll('a',{'class':'result-title hdrlnk'}):
            href=link.get('href')
            print(href)
            title=link.text
            print(title)

    page+=1

spider(1)