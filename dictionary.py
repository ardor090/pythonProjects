import re

try:  # python3
    from urllib.request import urlopen
except:  # python2
    from urllib import urlopen

try:
    url = "https://www.dictionary.com/browse/"
    word = input("Please Enter your Word: ")
    url = url + word
    data = urlopen(url).read()
    data1 = data.decode("utf-8")
    # print(data1)
    m = re.search('meta name = "definition" content ="', data1)
    start = m.end()
    end = m.start() + 300
    newString = data1[start:end]
    m = re.search("See more. ", newString)
    start = m.end()
    end = m.start() - 1
    definition = newString[start:end]
    print(definition)
except:
    print("Sorry word not in dictionary")
