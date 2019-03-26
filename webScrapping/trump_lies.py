import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('http://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

# Prints the first 500 characters
# print(r.text[0:500])

soup = BeautifulSoup(r.text, "html.parser")
# print(soup)
print(soup.prettify())

results = soup.findAll('span', attrs={'class': 'short-desc'})
# print(result[-1])
# print(len(result))

# first_result = results[0]

records = []
for result in results:

    textDate = result.find("strong").text[0:-1] + ', 2017'

    lie = result.contents[1][1:-2]
    # print(lie)

    # I can use any method to get the desired result
    # explanation = lie = first_result.contents[2]
    explanation = result.find("a").text[1:-1]
    # print(explanation)

    extract_url = result.find("a")["href"]
    # print(extract_url)

    records.append((textDate, lie, explanation,extract_url))
# print(records)

df = pd.DataFrame(records, columns=["textDate", "lie", "explanation", "extract_url"])

df["textDate"] = pd.to_datetime(df["textDate"])

df.to_csv('trump_lies.csv', index=None, encoding="utf-8")

