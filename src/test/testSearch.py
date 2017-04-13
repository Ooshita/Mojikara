# -*- coding: utf-8 -*-

import search
from json import loads

s = search.Search()

# with open("./sampleJson.json", "r", encoding="utf-8") as f:
#    json_dict = load(f)
# JSONをPython文字列に変換
body = s.execute("バイキンマン")
repos = loads(body)

# 画像のリンクを出力する.

for r in repos['items']:
    print(r['link'])
