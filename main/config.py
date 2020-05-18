import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "sqlite:///test.db"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY="secret key"


# or 演算子を使用して、os.environ.get('DATABASE_URL')が空文字だった場合,右辺を代入するようにしています。
# os.environ.get('DATABASE_URL')はherokuのpostgresで使用し、右辺はsqliteのデータベースです。
# こうすることでherokuの環境とローカルの環境で書き換える必要がありません。
#
# SECRET_KEYはセッション情報を暗号化するためのキーです。実際に運用する場合には、SECRET_KEYは必ず変更してください。
