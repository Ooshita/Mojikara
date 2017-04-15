import MeCab
from collections import Counter
keywords = []
m = MeCab.Tagger(' -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    
class Get_feature:
    # 起動時に一度だけ動く処理
    def __init__(self):
        self.document = ""
    
    def morph_result(document):
        for word in document:
            node = m.parseToNode(word).next
            while node:
                nodeFeature = node.feature.split(",")
                # 名詞,一般と名詞．名詞,固有名のみ抽出
                if nodeFeature[0] == "名詞" and nodeFeature[1] == "一般" or  nodeFeature[0] == "名詞" and nodeFeature[1] == "固有名詞":
                    keywords.append(node.surface)
                node = node.next
        return keywords

    def most_word(keywords):
        # 単語の頻出度を調べる
        word_dict = {}
        count_word = Counter(keywords)
        for word, cnt in count_word.most_common():
            # 単語（キー）と頻度を辞書に入れる
            word_dict.update({word:cnt})

        # 最大値のキーを表示
        most_key = ""
        for word, value in word_dict.items():
            if value == max(word_dict.values()):
                #print("最頻出単語: " + word) 
                most_key = word

        return most_key
