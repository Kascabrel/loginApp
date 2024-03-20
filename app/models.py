from app import db


def ini_db():
    """ Initialize the database """
    db.create_all()


class User(db.Model):
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.String(80), unique=True, nullable=False)
    password = db.column(db.String(80), nullable=False)

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
