from datetime import datetime
from time import sleep
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
from blog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}')"

    def set_password_hash(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Post (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(240))
    body = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"Post ('{self.id}', '{self.title}')"


class Rioni (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rione = db.Column(db.String(120), nullable=False)

    risultati = db.relationship('Risultati', backref='rioni', lazy=True)

    def __repr__(self) -> str:
        return f"Rioni ('{self.id}', '{self.rione}')"


class Risultati (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    posizione = db.Column(db.String(100))
    rioni_id = db.Column(db.ForeignKey('rioni.id'))
    gare_id = db.Column(db.ForeignKey('gare.id'))

    def __repr__(self) -> str:
        return f"Risultati ({self.id}', '{self.posizione}', '{self.rioni_id}', '{self.gare_id})"


class Gare (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.now())
    risultati = db.relationship('Risultati', backref='gare', lazy=True)

    def __repr__(self) -> str:
        return f"Gare ('{self.data}', '{self.risultati}', '{self.id})"


def insert_data():
    from datetime import datetime
    utente = User(created_at=datetime.now(), username='test',
                  email='test@test.com', password=generate_password_hash('test'))

    post1 = Post(author=utente, created_at=datetime.now(),
                 title='Primo Post', description='Prima Descirzione', body='testto tanto per')

    post2 = Post(author=utente, created_at=datetime.now(), title='Secondo Post',
                 description='Seconda Descirzione', body='testto tanto per')

    post3 = Post(author=utente, created_at=datetime.now(),
                 title='Terzo Post', description='Terza Descirzione', body='testto tanto per')

    rione1 = Rioni(rione='Portaccia')
    rione2 = Rioni(rione='Piazza')
    rione3 = Rioni(rione='Ponte Giorngini')
    rione4 = Rioni(rione='Marina')
    rione5 = Rioni(rione='Castello')
    rione6 = Rioni(rione='Null')

    from datetime import date
    gara1 = Gare(data=date(1953, 8, 15))
    gara2 = Gare(data=date(1954, 8, 15))
    gara3 = Gare(data=date(1955, 8, 15))
    gara4 = Gare(data=date(1956, 8, 15))

    # gara 1
    risultato11 = Risultati(posizione='Primo', gare=gara1, rioni=rione1)
    risultato12 = Risultati(posizione='Secondo', gare=gara1, rioni=rione2)
    risultato13 = Risultati(posizione='Terzo', gare=gara1, rioni=rione3)
    risultato14 = Risultati(posizione='Quarto', gare=gara1, rioni=rione4)
    risultato15 = Risultati(posizione='Quinto', gare=gara1, rioni=rione5)
    # gara 2
    risultato21 = Risultati(posizione='Primo', gare=gara2, rioni=rione2)
    risultato22 = Risultati(posizione='Secondo', gare=gara2, rioni=rione1)
    risultato23 = Risultati(posizione='Terzo', gare=gara2, rioni=rione5)
    risultato24 = Risultati(posizione='Quarto', gare=gara2, rioni=rione4)
    risultato25 = Risultati(posizione='Quinto', gare=gara2, rioni=rione3)
    # Gara 3
    risultato31 = Risultati(posizione='Primo', gare=gara3, rioni=rione5)
    risultato32 = Risultati(posizione='Secondo', gare=gara3, rioni=rione4)
    risultato33 = Risultati(posizione='Terzo', gare=gara3, rioni=rione3)
    risultato34 = Risultati(posizione='Quarto', gare=gara3, rioni=rione2)
    risultato35 = Risultati(posizione='Quinto', gare=gara3, rioni=rione1)

    db.session.add_all([risultato11,
                       risultato12,
                       risultato13,
                       risultato14,
                       risultato15,
                       risultato21,
                       risultato22,
                       risultato23,
                       risultato24,
                       risultato25,
                       risultato31,
                       risultato32,
                       risultato33,
                       risultato34,
                       risultato35]
                       )
    db.session.add(utente)

    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)

    db.session.add(rione1)
    db.session.add(rione2)
    db.session.add(rione3)
    db.session.add(rione4)
    db.session.add(rione5)
    db.session.add(rione6)

    db.session.commit()
