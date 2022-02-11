from flask import render_template
# Importa istanza di flask avviata dentro __init__.py
from blog import app

# Definizione delle rotte del sito 
@app.route ("/")
def homepage ():
    posts = [{"title": "Primo Post", "body": "Corpo del primo Post"},
            {"title": "Secondo Post", "body": "Corpo del secondo Post"}]
    return render_template ('homepage.html', posts = posts)

@app.route ('/about')
def about ():
        return render_template ('about_page.html')