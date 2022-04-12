from datetime import datetime
from time import sleep
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
from blog import db
from flask_login import UserMixin
from faker import Faker
from faker.providers import lorem
from flask_admin import Admin

# Imposta faker per riempire database
fake = Faker ('it_IT')
fake.add_provider (lorem)





class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f"User('{self.username}')"

    def set_password_hash(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Post (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable= False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(240))
    body = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"Post ('{self.title}')"


class Rioni (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rione = db.Column(db.String(120), nullable=False)
    immagine = db.Column(db.String (200))

    risultati = db.relationship('Risultati', backref='rioni', lazy=True)


    def __repr__(self) -> str:
        return f"Rioni ('{self.rione}')"


class Risultati (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ordine_id = db.Column(db.ForeignKey('ordine.id'))
    rioni_id = db.Column(db.ForeignKey('rioni.id'))
    gare_id = db.Column(db.ForeignKey('gare.id'))

    def __repr__(self) -> str:
        return f"Risultati ('{self.gare_id}')"


class Gare (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.now())
  
    risultati = db.relationship('Risultati', backref='gare', lazy=True)
    

    def __repr__(self) -> str:
        return f"Gare ('{self.data}')"
    
class Ordine (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classificato = db.Column(db.String(100))
    risultati = db.relationship('Risultati', backref='ordine', lazy=True)
    
    def __repr__(self) -> str:
        return f"Ordine ('{self.classificato}')"
    
    
    



def insert_data():
    from datetime import datetime
    utente = User(created_at=datetime.now(), username='test',
                  email='test@test.com', password=generate_password_hash('test'))

    post1 = Post(author=utente, created_at=datetime.now(),
                 title='Primo Post', description='Prima Descirzione', body= fake.paragraph (nb_sentences = 30))

    post2 = Post(author=utente, created_at=datetime.now(), title='Secondo Post',
                 description='Seconda Descirzione', body= fake.paragraph (nb_sentences = 30))

    post3 = Post(author=utente, created_at=datetime.now(),
                 title='Terzo Post', description='Terza Descirzione', body= fake.paragraph (nb_sentences = 30))

    rione1 = Rioni(rione='Portaccia')
    rione2 = Rioni(rione='Piazza')
    rione3 = Rioni(rione='Ponte Giorngini')
    rione4 = Rioni(rione='Marina')
    rione5 = Rioni(rione='Castello')
    rione6 = Rioni(rione='Null')
    
    ordine1 = Ordine (classificato = 'Primo')
    ordine2 = Ordine (classificato = 'Secondo')
    ordine3 = Ordine (classificato = 'Terzo')
    ordine4 = Ordine (classificato = 'Quarto')
    ordine5 = Ordine (classificato = 'Quinto')


    from datetime import date
    gara1 = Gare(data=date(1953, 8, 15))
    gara2 = Gare(data=date(1954, 8, 15))
    gara3 = Gare(data=date(1955, 8, 15))
    gara4 = Gare(data=date(1956, 8, 15))

    # gara 1
    risultato11 = Risultati(ordine = ordine1, gare=gara1, rioni=rione1)
    risultato12 = Risultati(ordine = ordine2, gare=gara1, rioni=rione2)
    risultato13 = Risultati(ordine = ordine3, gare=gara1, rioni=rione3)
    risultato14 = Risultati(ordine = ordine4, gare=gara1, rioni=rione4)
    risultato15 = Risultati(ordine = ordine5, gare=gara1, rioni=rione5)
    # gara 2
    risultato21 = Risultati(ordine = ordine1, gare=gara2, rioni=rione2)
    risultato22 = Risultati(ordine = ordine2, gare=gara2, rioni=rione1)
    risultato23 = Risultati(ordine = ordine3, gare=gara2, rioni=rione5)
    risultato24 = Risultati(ordine = ordine4, gare=gara2, rioni=rione4)
    risultato25 = Risultati(ordine = ordine5, gare=gara2, rioni=rione3)
    # Gara 3
    risultato31 = Risultati(ordine = ordine1, gare=gara3, rioni=rione5)
    risultato32 = Risultati(ordine = ordine2, gare=gara3, rioni=rione4)
    risultato33 = Risultati(ordine = ordine3, gare=gara3, rioni=rione3)
    risultato34 = Risultati(ordine = ordine4, gare=gara3, rioni=rione2)
    risultato35 = Risultati(ordine = ordine5, gare=gara3, rioni=rione1)

    db.session.add_all([ordine1,
                        ordine2,
                        ordine3,
                        ordine4,
                        ordine5]
                       )

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
