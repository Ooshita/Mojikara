# -*- coding: utf-8 -*-

import search
import get_feature_value
from collections import Counter
from json import loads

feature = get_feature_value.Get_feature
keywords = feature.morph_result("米軍が北朝鮮に軍事力を行使する場合に、出撃や後方支援の拠点になる在日米軍基地では、有事を想定したとみられる動きが出ている。")


# 単語の頻出度を調べる
word_dict = {}
count_word = Counter(keywords)
for word, cnt in count_word.most_common():
    # 単語（キー）と頻度を辞書に入れる
    word_dict.update({word:cnt})
    #print(word, cnt)


# 辞書の最大値を表示
# print(max(word_dict.values()))


# 最大値のキーを表示
most_key = ""
for word, value in word_dict.items():
    if value == max(word_dict.values()):
        #print("最頻出単語: " + word) 
        most_key = word

json = search.Search().execute(most_key)
repos = loads(json)
image_link = []
for r in repos['items']:
    image_link.append(r['link'])

# 最大値の単語で調べた画像のリンクを表示
print(image_link)
