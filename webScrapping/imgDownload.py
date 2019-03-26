import requests
from bs4 import BeautifulSoup
# from urllib.request import urlopen
import urllib
from csv import writer



# Setting up
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata
i = 1
soup = make_soup("https://uwaterloo.ca/")
for img in soup.findAll('img'):
    temp= img.get('src')
    if temp[:1] == "/":
        image = "https://uwaterloo.ca/" + temp
    else:
        image = temp

    nametemp = img.get("alt")
    if len(nametemp) == 0:
        filename = str(i)
        i+=1
    else:
        filename = nametemp

    imagefile = open(filename + ".jpeg","wb")
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()