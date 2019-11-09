from flask import Flask, render_template
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

app = Flask(__name__)

login = LoginManager()
login.init_app(app)
login.login_view = "users.login"

from myproject.users.users import users
from myproject.connection.connect import main

app.register_blueprint(users)
app.register_blueprint(main)
