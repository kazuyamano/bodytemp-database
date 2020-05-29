# viwes.pyが実行される際、main.modelsのEntryクラス（データベースのモデル）がimportされます

from main import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)
    #created_at =db.Column(db.DateTime) ←仮置き。日付投入用

    def __repr__(self):
        return "<Entry id={} title={!r}>".format(self.id, self.title)


def init():
    db.create_all()
