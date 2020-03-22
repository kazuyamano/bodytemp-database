import flask 
from main import app, db
from main import app
from main.models import Entry

# route() デコレータを使用し、ファンクションを起動するURLをFlaskに教えます。
# そのファンクション名は特定のファンクションに対してURLを生成するためにも使われ、 
# ファンクションはユーザーのブラウザ上で表示したいメッセージを返します。
# @app.route('/')
# def hello_world():
#     return "Hello World!"

@app.route('/')
def show_entries():
    entries = Entry.query.all()
    return flask.render_template('entries.html', entries=entries)


# add_entry 関数の追加
@app.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(
        title = flask.request.form['title'],
        text = flask.request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    return flask.redirect(flask.url_for('show_entries'))
