import flask 
from main import app, db
from main.models import Entry

@app.route('/')
def show_entries():
    entries = Entry.query.all()
    return flask.render_template('entries.html', entries=entries)


# htmlにフォームを設置し、そこからDBへ追加できるようにします。add_entry 関数の追加
@app.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(
        title = flask.request.form['title'],
        text = flask.request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    return flask.redirect(flask.url_for('show_entries'))
