from flask_wtf import FlaskForm, RecaptchaField
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired
from wtforms import ValidationError
# from captcha.image import ImageCaptcha

# image = ImageCaptcha()

# ----- add captcha here to
# data = image.generate('1234')
# image.write('1234', 'out.png')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Login')
