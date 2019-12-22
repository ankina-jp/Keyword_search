import requests as web
import bs4
import re
from mysql import mysql_conect_class as mc

#キーワード設定
list_keywd = ['キッチンスタジオ']

#url設定　num=...最大検索数　　start=...検索順位開始値
resp = web.get('https://www.google.co.jp/search?num=100&start=0&q=' + ''.join(list_keywd))

#検索時にエラーが発生した場合停止する
resp.raise_for_status()

#ページをすべて読み込む
soup = bs4.BeautifulSoup(resp.text, "html.parser")

#class別で要素を取得
title = soup.select(".BNeawe.vvjwJb.AP7Wnd")
url = soup.select(".BNeawe.UPmit.AP7Wnd")
description = soup.select(".BNeawe.s3v9rd.AP7Wnd")

#タグの除去
p = re.compile(r"<[^>]*?>")


count = 0
for title, url, description in zip(title, url, description):
    #掲載順にランク付け
    count += 1
    
    #属性の変更
    row_title = p.sub("",title.text)
    row_url = p.sub("",url.text)
    row_description = p.sub("",description.text)
    
    #sqlを準備
    data = mc.sql_execution_group('keyword_search_db',"INSERT INTO `search_key_kitchen_studio`(`Title`, `Url`, `Description`, `Ranking`) VALUES ('" + row_title[:250] + "','" + row_url[:250] + "','" + row_description[:250] + "'," + str(count) + " )")
    #sql実行
    rows = data.Sql_Controller()

#結果表示
for row in rows:
    print(row)