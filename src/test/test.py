# -*- coding: utf-8 -*-

import search
import get_feature_value
from collections import Counter
from json import loads

feature = get_feature_value.Get_feature
keywords = feature.morph_result("米軍が北朝鮮に軍事力を行使する場合に、出撃や後方支援の拠点になる在日米軍基地では、有事を想定したとみられる動きが出ている。")

# keywordsディクショナリーから最大値を取得する
most_word = feature.most_word(keywords)

json = search.Search().execute(most_word)
repos = loads(json)
image_link = []
for r in repos['items']:
    image_link.append(r['link'])

# 最大値の単語で調べた画像のリンクを表示
print(image_link)
