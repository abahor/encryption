from flask import Flask,render_template
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import Email, EqualTo, DataRequired
from wtforms import ValidationError
from pyfladesk import init_gui

app = Flask(__name__)

login_manager.login_view = "users.login"

from myproject.login.users import users

app.register_blueprint(users)

# if __name__ == '__main__':
#     init_gui(app)
