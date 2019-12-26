import requests
from bs4 import BeautifulSoup
#from urllib.parse import urljoin

domain = "https://totta.xsrv.jp"

# スクレイピング対象の URL にリクエストを送り HTML を取得する
res = requests.get(domain)
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select("a[href]")
result = []

for a in links:
    href = a.attrs['href']
#    dalate_domain = href.replace(domain,'')

#    if not dalate_domain in result:
#        result.append(dalate_domain)

    if not href in result:
        result.append(href)

result_in_not = [delete for delete in result if 'mailto:' not in delete
                 and 'tel:' not in delete]

print(result_in_not)