# viwes.pyが実行される際、main.modelsのEntryクラス（データベースのモデル）がimportされます

from main import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jcode = db.Column(db.String(7))
    temp = db.Column(db.String(4))
    date =db.Column(db.DateTime)
    
    def __init__(self, jcode=None, temp=None):
        self.jcode= jcode
        self.temp= temp
        self.date= datetime.utcnow()



def init():
    db.create_all()

