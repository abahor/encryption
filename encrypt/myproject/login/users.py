from myproject.users.forms import RegisterationForm, LoginForm, yourEmail
from flask import redirect, render_template, Blueprint, url_for, session, request, flash, abort
from flask_login import login_required, login_user, logout_user, current_user
import requests

users = Blueprint('users', __name__, template_folder='temp')


@users.route('/')
def main():
    form = LoginForm()
    if current_user.is_authenticated:
        redirect('/connect')
    if form.validate_on_submit():
        # user = Users.query.filter_by(email=form.email.data).first()
        req = requests.Session()
        data = {'username':form.email.data,'password':form.password.data}
        d = req.post('https://webserver.com/verify',data)# -- it should be https ---- put the webserver name
        if d.status_code == 200 :
            login_user(user, remember=True, duration=datetime.timedelta(weeks=52))
        else:
            flash('password is wrong')

    return render_template('main.html',form=form)

@users.route('/register')
def register():
    return render_template('register.html') # ---- OPEN A URL IN THE BROWSER TO THE SERVER TO REGISTER

@users.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        req = requests.Session()
        paramed = {'c': form.email.data}
        username = req.post('https://www.secure.com/username',params = paramed)
        if  username.response:
            params = {'c': form.password.data }
            # -- username stored in the Session['username']
            password = req.post('https://www.secure.com/password',params = params)
            # -- limiter for the password route in the server
            if password.response:
                login_user(current_user)
                redirect('/connect')
        else:
            flash("email doesn't exist")
    return render_template('login.html',form)
