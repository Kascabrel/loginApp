from app import db


def ini_db():
    """ Initialize the database """
    db.create_all()
    admin = User('admin', 'admin@volkswagen.com', 'pseudo_admin')
    guest = User('guest', 'guest@volkswagen.com', 'pseudo_guest')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    db.create_all()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    pseudo = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password, pseudo):
        self.username = username
        self.password = password
        self.pseudo = pseudo

    def __repr__(self):
        return f'<User :{self.username}>'




