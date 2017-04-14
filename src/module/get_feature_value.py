import MeCab
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
