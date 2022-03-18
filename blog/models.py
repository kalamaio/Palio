from datetime import datetime
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
from blog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user (id):
    return User.query.get(int(id))

class User (db.Model,UserMixin):
    id = db.Column ( db.Integer, primary_key = True)
    created_at = db.Column ( db.DateTime, default = datetime.now) 
    username = db.Column ( db.String(20), unique = True, nullable = False)
    email = db.Column ( db.String(50), unique = True, nullable = False)
    password = db.Column ( db.String(250), nullable = False )
    posts = db.relationship ( 'Post', backref = 'author', lazy = 'dynamic')
    
    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}')"
    
    def set_password_hash ( self, password):
        self.password = generate_password_hash ( password)
    
    def check_password ( self, password):
        return check_password_hash ( self.password, password)
    
    
class Post ( db.Model):
    id = db.Column ( db.Integer, primary_key = True)
    user_id = db.Column ( db.Integer, db.ForeignKey('user.id'), nullable = False)
    created_at = db.Column ( db.DateTime, default = datetime.now)
    title = db.Column ( db.String(120), nullable = False)
    description = db.Column ( db.String(240))
    body = db.Column ( db.Text(), nullable = False )
    
    def __repr__(self):
        return f"Post ('{self.id}', '{self.title}')"
    
    
class Rioni (db.Model):
    id = db.Column ( db.Integer, primary_key = True)
    rione = db.Column ( db.String(120), nullable = False)
    gare = db.relationship('Gare', backref='rioni', lazy=True)
    def __repr__(self) -> str:
        return f"Rioni ('{self.rione}', '{self.gare})"

    
    
    def __repr__ (self):
        return f"Rioni ('{self.id}', '{self.rione}')"
    

class Gare (db.Model):
    id = db.Column ( db.Integer, primary_key = True)
    data = db.Column ( db.Date, default = datetime.now())
    primo = db.Column (db.Integer)
    secondo = db.Column (db.Integer)
    terzo = db.Column (db.Integer)
    quarto = db.Column (db.Integer)
    quinto = db.Column (db.Integer)
    valido = db.Column ( db.Boolean, default= True, nullable = False)
    rioni_id = db.Column (db.Integer, db.ForeignKey('rioni.id'))
    
    def __repr__(self) -> str:
        return f"Gare ('{self.data}', '{self.primo}', '{self.secondo}', '{self.terzo}', '{self.quarto}', '{self.quinto}', '{self.valido}', '{self.rioni_id})"
    
    
def insert_data ():
    from datetime import datetime
    utente = User ( created_at = datetime.now(), username = 'test', email ='test@test.com', password = generate_password_hash ('test'))
    
    post1 = Post (author = utente, created_at = datetime.now(), title = 'Primo Post', description = 'Prima Descirzione', body = 'testto tanto per')
    post2 = Post (author = utente, created_at = datetime.now(), title = 'Secondo Post', description = 'Seconda Descirzione', body = 'testto tanto per')
    post3 = Post (author = utente, created_at = datetime.now(), title = 'Terzo Post', description = 'Terza Descirzione', body = 'testto tanto per')
    
    rione1 = Rioni (rione = 'Portaccia')
    rione2 = Rioni (rione = 'Piazza')
    rione3 = Rioni (rione = 'Ponte Giorngini')
    rione4 = Rioni (rione = 'Marina')
    rione5 = Rioni (rione = 'Castello')
    rione6 = Rioni (rione = 'Null')
    
    from datetime import date
    primo = Gare (data= date(1953, 8, 15), primo = 1, secondo = 2, terzo = 4, quarto = 5, quinto = 3, rioni = rione1)
    secondo = Gare (data= date(1954, 8, 15), primo = 2, secondo = 1, terzo = 5, quarto = 4, quinto = 3, rioni = rione2)
    terzo = Gare (data= date(1955, 8, 15), primo = 3, secondo = 2, terzo = 4, quarto = 5, quinto = 1, rioni = rione3)
    quarto = Gare (data= date(1956, 8, 15), primo = 3, secondo = 2, terzo = 4, quarto = 5, quinto = 1, rioni= rione4)
    
    
    db.session.add (utente)
    
    db.session.add (post1)
    db.session.add (post2)
    db.session.add (post3)
    
    db.session.add (rione1)
    db.session.add (rione2)
    db.session.add (rione3)
    db.session.add (rione4)
    db.session.add (rione5)
    db.session.add (rione6)
    
    db.session.add (primo)
    db.session.add (secondo)
    db.session.add (terzo)
    db.session.add (quarto)

    db.session.commit ()
      