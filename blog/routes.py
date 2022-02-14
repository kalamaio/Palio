from flask import render_template
# Importa istanza di flask avviata dentro __init__.py
from blog import app
# Importa istanza di Post
from blog.models import Post, Gare

# Definizione delle rotte del sito 
@app.route ("/")
def homepage ():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template ('homepage.html', posts = posts)

@app.route ('/palio')
def palio ():
    palii = Gare.query.order_by(Gare.data.asc()).all()
    return render_template ('palio_lista.html', palii = palii)
    

@app.route ('/about')
def about ():
        return render_template ('about_page.html')