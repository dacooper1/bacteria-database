from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

import csv

db = SQLAlchemy()

bcrypt = Bcrypt()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(UserMixin, db.Model):
    """Playlist."""
    # ADDING HASHING METHOD
    # ADD THE NECESSARY CODE HERE

    @classmethod
    def register(cls, username, pwd):
        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode("utf8")

        return cls(username=username, password=hashed_utf8)
    
    @classmethod
    def authenticate(cls, username, pwd):
        u = User.query.filter_by(username=username).first()
        if u and bcrypt.check_password_hash(u.password, pwd):
            return u 
        else:
            return False
        
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)

    first_name = db.Column(db.String, nullable = False)

    last_name = db.Column(db.String, nullable = False)

    username = db.Column(db.String, nullable = False, unique=True)

    password = db.Column(db.String, nullable=False)


    def __repr__(self):
        """Displaying User"""

        u = self 
        return f"<id={u.id}, first name={u.first_name}, last name={u.last_name}, username ={u.username}>"
    
class Bacterium(db.Model):
    """Playlist."""

    # @classmethod
    # def add_genus_index(cls):
    #     with open('A.csv', newline='') as csvfile_a:
    #         list = [];
    #         file = csv.DictReader(csvfile_a)
    #         for row in file:
    #             list.append(row['species'])
    #         print(list)
    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'bacteria'

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)

    genus = db.Column(db.String, nullable = False)

    species = db.Column(db.String, nullable = False)

    strain_id = db.Column(db.Integer)


    def __repr__(self):
        """Displaying User"""

        u = self 
        return f"<id={u.id}, genus={u.genus}, species={u.species}, strain_id ={u.strain_id}>"

class Favourite(db.Model):
    """Playlist."""
   
    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'favourites'

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))

    bacterium_id = db.Column(db.Integer, db.ForeignKey('bacteria.id'))

    user = db.relationship('User', backref='favourites', passive_deletes=True)

    bacterium = db.relationship('Bacterium', backref='favourites')

    def __repr__(self):
        """Displaying User"""

        u = self 
        return f"<id={u.id}, user id={u.user_id}, bacterium id={u.bacterium_id}>"
