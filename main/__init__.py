# まず、 Flask クラスをインポートしました。このクラスのインスタンスは WSGIアプリケーションです。
#[このアプリケーションのモジュール名について]
# もしあなたが使うモジュールが一つだけなら、 __name__ を使わなければなりません。
# それがアプリケーションとして起動したときとモジュールとしてインポートされたときで名前が異なるからです
#  (アプリケーションとして起動したときは '__main__' 、インポートされたときはそのインポート名)
# from flask import Flask

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

# 次にインスタンスを生成します。モジュールやパッケージの名前は要りません。このインスタンスは
# Flaskがテンプレートファイルやスタティックファイルなどをどこから探すのかを認識するために必要です。
# app = Flask(__name__)
app = Flask(__name__)
app.config.from_object('main.config')
db = SQLAlchemy(app)

import main.views
