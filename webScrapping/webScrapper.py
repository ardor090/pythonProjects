# import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as b

# base_url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="
# request = "ps4"
# url_operator = "&_sacat=0&_pgn="
# page_num = "2"
#
# url = base_url + request + url_operator + page_num

url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=xbox&_sacat=0&LH_TitleDesc=0&_pgn=2"

html = urlopen(url).read()
html1 = html.decode("utf-8")

print(html1)