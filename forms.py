from wtforms import SelectField, StringField, TextAreaField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Optional

class RegisterForm(FlaskForm):
    first_name = StringField("FIRST NAME", validators=[InputRequired()], render_kw={'class': 'user-form'})
    last_name = StringField("LAST NAME", validators=[InputRequired()], render_kw={'class': 'user-form'})
    username = StringField("USERNAME", validators=[InputRequired()], render_kw={'class': 'user-form'})
    password = PasswordField("PASSWORD", validators=[InputRequired()], render_kw={'class': 'user-form'})

class LoginForm(FlaskForm):
    username = StringField("USERNAME", validators=[InputRequired()], render_kw={'class': 'user-form'})

    password = PasswordField("PASSWORD", validators=[InputRequired()], render_kw={'class': 'user-form'})

