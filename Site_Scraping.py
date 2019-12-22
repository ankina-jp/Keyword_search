import requests
from bs4 import BeautifulSoup

address = 'https://www.sakanoue-st.net/'
resp = requests.get(address)
data = resp.text

soup = BeautifulSoup(data, 'lxml')

for obj in soup.body.children:
    print(soup.prettify())
    if (obj.name !=None):
        try:
            print(obj.name + " class=" + str(obj['class']))
        except KeyError:
            print(obj.name + "**not class**")
