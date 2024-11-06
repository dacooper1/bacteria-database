from flask import Flask, redirect, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from my_secrets import USER, API_SECRET_KEY

from models import db, connect_db, User, Favourite, Bacterium
from forms import RegisterForm, LoginForm
import bacdive



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.sdcpbhigcagexurbnwgi:degbo2-xYnpav-jupkos@aws-0-ca-central-1.pooler.supabase.com:6543/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
app.app_context().push()
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

client = bacdive.BacdiveClient(USER, API_SECRET_KEY)



app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route('/')
def root():
    return redirect('/index')

@app.route('/index')
def show_home_page():
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return render_template('home.html', alphabet=alphabet)

@app.route('/index/<letter>')
def show_letter_index(letter):
    list = Bacterium.query.filter(Bacterium.species.startswith(letter)).order_by(Bacterium.species).all()
    return render_template('letter_index', list=list, letter=letter)

@app.route('/index/<int:id>')
def show_species_data(id):
    bacteria = Bacterium.query.get_or_404(id)
    bacdive_id = bacteria.strain_id
    bacdive_bacteria_search = client.search(id=bacdive_id)
    bacdive_bacteria_data = None

    for strain in client.retrieve():
        bacdive_bacteria_data = strain
    


    return render_template('species_data.html', bacteria=bacteria, data=bacdive_bacteria_data)

@app.route('/login', methods=['GET', 'POST'])
def show_login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        pwd = form.password.data

        user = User.authenticate(username, pwd)

        if user:
            session['user_id'] = user.id
            return redirect('/')
        else:
            form.username.errors = ['Incorrect username/password, please try again.']
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def show_register():
    form = RegisterForm()

    if form.validate_on_submit():
        f_name = form.first_name.data
        l_name = form.last_name.data
        username = form.username.data
        pwd = form.password.data
        user = User.register(username,pwd)
        user.first_name = f_name
        user.last_name = l_name

        db.session.add(user)
        db.session.commit()

        session['user_id']=user.id

        return redirect('/')
    else:
        return render_template('register.html', form=form)


    
