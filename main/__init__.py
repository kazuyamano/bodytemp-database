# run.pyで、mainディレクトリのパッケージがimportされた際にこのスクリプトが実行されます。

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy　 #PostgreSQL向け追加

app = Flask(__name__)
app.config.from_object('main.config') 　 #PostgreSQL向け追加

db = SQLAlchemy(app) 　 #PostgreSQL向け追加

import main.views




#_init_.pyの働きに関してはこちらがわかりやすかったです。
# https://www.kangetsu121.work/entry/2018/09/16/004008
#  ↓引用
#[__init__.py の機能]
# まず、__init__.py が存在するディレクトリを、Pythonにパッケージとして認識させるという機能があります。
# パッケージとは、複数の py ファイルをまとめたもの。
# また、パッケージの中の pyファイルを モジュール と呼び、パッケージ丸ごとでなくモジュール単位での importも可能です。
# つまり、__init__.py ファイルをディレクトリに置くことで、そのディレクトリ内の pyファイルは import して別の pyファイルから利用可能となる。
#
# もう一つの機能が、importされた際に __init__.py に記述されたスクリプトが実行されるというものです。
# __init__.py という名前からすると、こちらの機能は initialize 処理っぽくてしっくりきますね。
