from flask import Flask, redirect, render_template, session, request
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager, login_required, login_user
from dotenv import load_dotenv
import os

from models import db, connect_db, User, Favourite, Bacterium
from forms import RegisterForm, LoginForm
import bacdive

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

if __name__ == "__main__":
    # Use the port provided by the environment, or default to 5000 if not set
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

connect_db(app)
app.app_context().push()

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'show_login' 

db.create_all()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

client = bacdive.BacdiveClient(os.getenv('BACDIVE_USER'),os.getenv('API_SECRET_KEY'))



app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@login_manager.user_loader
def load_user(user_id):
    # Fetch the user by ID from the database
    return User.query.get(user_id)

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
    return render_template('letter_index.html', list=list, letter=letter)

@app.route('/species/<int:id>')
@login_required
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
            login_user(user)

            next_page = request.args.get('next')

            return redirect(next_page or  '/')
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

        login_user(user)

        return redirect('/')
    else:
        return render_template('register.html', form=form)


    
