import flask
import sqlite3
import os

# Create application instance
app = flask.Flask(__name__)

# Specify the file from which config should be loaded from
# Here, we are loading config from this file (i.e. app.py)
app.config.from_object(__name__)

app.config.update(dict(
        DATABASE = os.path.join(app.root_path, 'database.db'),
        USERNAME='admin',
        PASSWORD='default',
        SECRET_KEY='development key',
    ))

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    # Make rows to be used as deictionaries instead of tuples
    rv.row_factory = sqlite3.Row
    return rv

@app.route("/")
def show_entries():
   return "hello" 
