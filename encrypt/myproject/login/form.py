from flask_wtf import FlaskForm,RecaptchaField
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired
from wtforms import ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder':'Email'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder':'Password'})
    submit = SubmitField('Login')


class RegisterationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()], render_kw={'placeholder': 'Email'})
    username = StringField('username', validators=[InputRequired()], render_kw={'placeholder': 'Username'})
    password = PasswordField('Password',
                             validators=[InputRequired(), EqualTo('pass_confirm', message='Passwords must match')],
                             render_kw={'placeholder': 'Password'})
    pass_confirm = PasswordField('Confirm Password',
                                 validators=[InputRequired()], render_kw={'placeholder': 'confirm password'})
    # recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    def check_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('This email is already exists login instead')


# ---------------------------- yourEmail ---------------------------

class yourEmail(FlaskForm):
    email = StringField('your email',validators=[DataRequired(),Email()],render_kw={"placeholder":'your Email'})
    submit = SubmitField('send')
