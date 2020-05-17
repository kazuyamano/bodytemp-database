from main import db
from flask_sqlalchemy import SQLAlchemy


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return "<Entry id={} jcode={!r}>".format(self.id, self.jcode)


def init():
    db.create_all()
