from flask import render_template, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user, login_required
# Importa istanza di flask avviata dentro __init__.py
from blog import app
# Importa istanza di Post
from blog.models import Post, Gare, User, Rioni
# Importa form di login
from blog.forms import LoginForm

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
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("homepage"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username='testina').first()
        if user is None or not user.check_password(form.password.data):
            flash("username e password non combaciano!")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("homepage"))
    return render_template("login.html", form=form)

@app.route ("/logout")
def logout():
    logout_user()
    return redirect ( url_for("homepage"))