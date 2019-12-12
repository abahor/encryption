from functools import wraps

from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykeyasdfghjklsdfghnjm'
# app.debug = True

login = LoginManager()
login.init_app(app)
login.login_view = "main.login"





from myproject.users.users import users
from myproject.connection.views import main

app.register_blueprint(users)
app.register_blueprint(main)
