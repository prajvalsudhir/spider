import random
import urllib.request

def downimage(url):
    num=random.randrange(1,2000)
    site=str(num)+".png"
    urllib.request.urlretrieve(url,site)


downimage("https://i.kym-cdn.com/photos/images/newsfeed/001/176/251/4d7.png")
