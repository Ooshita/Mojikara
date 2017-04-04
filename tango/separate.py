import sys
import MeCab
import os
import codecs

m = MeCab.Tagger(' -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

text = sys.argv[1]
keywords = []
with codecs.open(os.path.join('./', text),'r', 'utf-8') as f:
    context = f.read()
    #encoded_text = context.encode('utf-8')
    node = m.parseToNode(context).next
    while node:
        # 名詞,一般の行だけを抽出する．
        if node.feature.split(",")[0] == "名詞" and node.feature.split(",")[1] == "一般":
            if node.surface not in keywords:
                keywords.append(node.surface)
        node = node.next
    print(' '.join(keywords))
