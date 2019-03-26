import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.jumia.com.ng/")

soup = BeautifulSoup(r.text, "html.parser")

print(soup)