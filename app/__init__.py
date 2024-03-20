from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cli import cli
from flask.cli import with_appcontext

app = Flask(__name__)
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)


@app.cli.command('init_db')
@with_appcontext
def init_db():
    """ Initialize the database """
    from app.models import ini_db
    ini_db()


@app.route('/')
def wellcome():
    return 'Hello World!'


# for initializing the database in the command line


if __name__ == '__main__':
    app.run(debug=True)
