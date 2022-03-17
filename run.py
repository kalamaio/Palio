from blog import app, db
from blog.models import User, Post, Rioni, Gare

# Importa database e classi User Post nella shell di flask

@app.shell_context_processor
def meke_shell_context():
    return {'db' : db, 'User' : User, 'Post' : Post, 'Rioni' : Rioni, 'Gare' : Gare}
