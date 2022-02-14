from datetime import datetime
from time import strftime
from werkzeug.security import generate_password_hash, check_password_hash
from blog import db


class User (db.Model):
    id = db.Column ( db.Integer, primary_key = True)
    created_at = db.Column ( db.DateTime, default = datetime.now) 
    username = db.Column ( db.String(20), unique = True, nullable = False)
    emailk = db.Column ( db.String(50), unique = True, nullable = False)
    password = db.Column ( db.String(250), nullable = False )
    posts = db.relationship ( 'Post', backref = 'author', lazy = 'dynamic')
    
    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.emailk}')"
    def set_password_hash ( self, password):
        self.password = generate_password_hash ( password)
    
    def check_pasword ( self, password):
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
    gare = db.relationship ( 'Gare', backref = 'gara', lazy = 'dynamic')
    
    def __repr__ (self):
        return f"Rioni ('{self.id}', '{self.rione}')"
    
    
class Gare (db.Model):
    id = db.Column ( db.Integer, primary_key = True)
    data = db.Column ( db.DateTime, default = datetime.now)
    numero_corsa = db.Column ( db.Integer)
    rione_id = db.Column ( db.Integer, db.ForeignKey('rioni.id'), nullable = False)
    valido = db.Column ( db.Boolean, default= True, nullable = False)
    
    def __repr__(self) -> str:
        return f"Gare ('{self.data(strftime ('%Y'))}', '{self.numero_corsa}')"