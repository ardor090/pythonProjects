from urllib.request import urlopen
from bs4 import BeautifulSoup as bS

my_url = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=grapics+card&ignorear=0&N=-1&isNodeId=1"

# Opening connection, Grabbing the page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

page_soup = bS(page_html, "html.parser")

# print(page_soup)

# print(page_soup.h1)
# print(page_soup.body.span)

# Grab each container
containers = page_soup.findAll("div", {"class":"item-container"})
# print(len(containers))
# print(containers[0])

container = containers[0]

shipping_container = container.findAll("li", {"class":"price-ship"})
print(shipping_container)

# print(title_container)
# print(title_container[0].text)
# for container in containers:
#     # brand = container.div.a.img["title"]
#
#     title_container = container.findAll("a", {"class": "item-title"})
#     product_name = title_container[0].text
#     print(container)

