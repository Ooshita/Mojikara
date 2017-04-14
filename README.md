Mojikarai  
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

あとはimportとしてご使用ください．  
  
実際のサンプルはsrcディレクトリ以下のtestディレクトリのtest.pyを参考にしてください．


## ライセンス  
[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)  

## 著作者  
[Ooshita](https://github.com/Ooshita)

