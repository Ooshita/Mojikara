Mojikara   
====
Pythonで書かれた，文章から画像のリンクを返す為のモジュール
  
## 説明  
このプログラム群はPythonで書かれた文章から特徴量を抽出して，そのワードに関連する画像のリンクを検索するものです．  
画像検索にはgoogleのCustom Search APIを使用しています．
そのapiの詳細は[公式ドキュメント](https://developers.google.com/custom-search/docs/overview?hl=ja)をご覧ください.  

実際の特徴量選択については現在考えておりますが，TF IDFにて重み付けされた単語を使用してみましたが，あまりいい精度が出ませんでした．現在は単純に頻出度の最大値で画像検索をしております．近いうちにもっと良い方法に変更するかもしれません．  
  

## 使用方法  
※このプログラムでは説明文にあるように，Custom Search APIを使用していますので，クライアントIDとエンジンIDを取得する必要があります．　　
  
環境変数PYTHONPATHにmoduleのパスを追加してください.  

[例]  

```
  export PYTHONPATH = '/Users/Ooshita/Mojikara/src/module/'
```

あとはimportしてご使用ください.  
[import例]    
====  
```python
import search # 絶対必要なモジュール
import get_feature_value # 絶対必要なモジュール
from collections import Counter
from json import loads
```
  
[具体的な使い方例]  
====  
```python
feature = get_feature_value.Get_feature
# 文章を形態素解析して得られた名詞（キー）と頻出度の数(バリュー)を辞書として返します.
keywords = feature.morph_result("米軍が北朝鮮に軍事力を行使する場合に、出撃や後方支援の拠点になる在日米軍基地では、有事を想定したとみられる動きが出ている。")

# keywordsディクショナリーから最大値を取得する
most_word = feature.most_word(keywords)
```
  
[最大頻出ワードの画像リンクを取得する]  
====  
```python
#importの追加
from json import loads

#最大頻出ワードをCustom Search APIを使用してjsonをGETする．
json = search.Search().execute(most_word)
repos = loads(json)
image_link = []
for r in repos['items']:
    # image_linkリストに画像のリンクをappend（追加）する.
    image_link.append(r['link'])
```
  
実際のサンプルはsrcディレクトリ以下のtestディレクトリのtest.pyを参考にしてください．
随時変更するかもしれないので，test.pyが最新のサンプルです．  


## ライセンス  
[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)  

## 著作者  
[Ooshita](https://github.com/Ooshita)

