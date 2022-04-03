
from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
# Importa istanza di flask avviata dentro __init__.py
from blog import app, login_manager
# Importa istanza di Post
from blog.models import Post, Gare, User, Rioni, Risultati
# Importa form di login
from blog.forms import LoginForm



#definizione login per parti sito dove il login è obbligo
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
#definizione login per parti sito dove il login è obbligo
@login_manager.unauthorized_handler
def unauthorized_callback(): 
    return redirect(url_for('login'))


# Definizione delle rotte del sito 
@app.route ("/")
def homepage ():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template ('homepage.html', posts = posts)

@app.route ("/post/<int:post_id>")
@login_required
def post_dettaglio (post_id):
    post= Post.query.get_or_404 (post_id)
    return render_template ('post_dettaglio.html', post= post)

@app.route ('/palio')
def palio ():
    date= Gare.query.order_by (Gare.data.asc()).all()
    pali = []
    for data in date:
        pali_list = Risultati.query.filter (Risultati.gare_id == data.id).order_by (Risultati.ordine_id.asc ()).all()
        pali.append (pali_list)
        
    return render_template ('palio_lista.html', risultati = pali, date = date)

'''@app.route ('/palio/<int:palio_id>/singolo', methods=['GET', 'POST'])
def palio_dettaglio (palio_id):
    
    risultati = Risultati.query.filter_by(gare_id = palio_id).all()
    #anno = Gare.query.filter_by (Gare.id == palio_id).first()
   
    return render_template ('palio_dett.html', gara= risultati)'''

@app.route ('/about')
def about ():
        return render_template ('about_page.html')
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("homepage"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username='test').first()
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

