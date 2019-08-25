import requests
import operator
from bs4 import BeautifulSoup

def freq(url):
    list1=[]
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    for i in soup.findAll('a',{'class':'result-title hdrlnk'}):
        con=i.string
        words=con.lower().split()
        for n in words:
            list1.append(n)
    print(list1)

freq('https://seattle.craigslist.org/search/jjj')

