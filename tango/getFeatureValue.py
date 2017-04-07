import sys
import os
import codecs
import numpy as np
import MeCab
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction import DictVectorizer
from collections import Counter

count = CountVectorizer()
keywords = []
m = MeCab.Tagger(' -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

def result(threshold):
    hairetsu = np.where(tfidf_array >= threshold)
    hit_word = np.unique(np.append(hairetsu[0], hairetsu[1]))
    word = []
    # tfidfで計算された単語を出力する．
    for num in range(0, len(hit_word)):
        word.append(feature[hit_word[num]])
    return word

def morphResult():
    for word in docs:
        node = m.parseToNode(word).next
        while node:
            nodeFeature = node.feature.split(",")
            # 名詞,一般と名詞．名詞,固有名のみ抽出
            if nodeFeature[0] == "名詞" and nodeFeature[1] == "一般" or  nodeFeature[0] == "名詞" and nodeFeature[1] == "固有名詞":
                keywords.append(node.surface)
            node = node.next
    return keywords

with codecs.open(os.path.join('./', sys.argv[1]), 'r', 'utf-8') as f:
    docs = np.array([f.read()])
    bag = count.fit_transform(docs)

# tfidfの設定
tfidf = TfidfTransformer(use_idf=True, norm='l2', smooth_idf=True)
# 小数点第4位まで表示する．
np.set_printoptions(precision=4)
cnt_voc = count.vocabulary_
tfidf_array = np.array(tfidf.fit_transform(bag).toarray())

# ベクトルと単語を対応づけるために必要な処理．
vec = DictVectorizer()
vec.fit_transform(cnt_voc).toarray()
feature = vec.get_feature_names()

word = []
word = result(0.3)
# 出力結果がなかった場合，閾値を下げる
if len(word) == 0:
    # それでも0だったら閾値をさらに下げる．
    if result(0.2) == 0:
        print(result(0.1))
    else:
        print(result(0.2))
else:
    print(word)

word_dict = {}
# 単語の頻出度を調べる
countWord = Counter(morphResult())
for word, cnt in countWord.most_common():
    word_dict.update({word:cnt})
    # print(word, cnt)

# 辞書の最大値を表示
# print(max(word_dict.values()))


# 最大値のキーを表示
for word, value in word_dict.items():
    if value == max(word_dict.values()):
        print(word)   
    

