from flask_wtf import FlaskForm,RecaptchaField
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired
from wtforms import ValidationError
