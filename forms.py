from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, ValidationError

def password_requirements(form, field):
    password = field.data
    errors = []
    
    if len(password) < 8:
        errors.append("at least 8 characters")
    if not any(char.isupper() for char in password):
        errors.append("at least one uppercase letter")
    if not any(char.islower() for char in password):
        errors.append("at least one lowercase letter")
    if not any(char.isdigit() for char in password):
        errors.append("at least one digit")
    
    if errors:
        raise ValidationError(f"Password must contain {', '.join(errors)}.")

class RegisterForm(FlaskForm):
    first_name = StringField("FIRST NAME", validators=[InputRequired()], render_kw={'class': 'user-form'})

    last_name = StringField("LAST NAME", validators=[InputRequired()], render_kw={'class': 'user-form'})

    username = StringField("USERNAME", validators=[InputRequired()], render_kw={'class': 'user-form'})

    password = PasswordField("PASSWORD", validators=[InputRequired(), password_requirements], render_kw={'class': 'user-form'})

class LoginForm(FlaskForm):
    username = StringField("USERNAME", validators=[InputRequired()], render_kw={'class': 'user-form'})

    password = PasswordField("PASSWORD", validators=[InputRequired()], render_kw={'class': 'user-form'})

