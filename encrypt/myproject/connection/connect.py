from flask import redirect, render_template, Blueprint, url_for, session, request, flash, abort
from flask_login import login_required, login_user, logout_user, current_user
import requests
from Crypto.Cipher import RSA

connect = Blueprint('connect', __name__, template_folder='temp')

# -- i will need to define a request.Session for the hole routes

# -- there must be a gereal request method here to handle all the cookies for each app

@connect.route('/connect')
@login_required
def connect():

    return render_template('main.html')


@connect.route('/got_connected')
def got_connected():

    # ---  all the chat will happen here in this page
    # --- request object initialization 
    return 's'

@connect.route('/call')
@login_required
def call():
    # -- open a conversation (chat) between two people
    return render_template('call.html')

# -- future route call () video() voice() media()

@connect.route('/encrypt')
@login_required
def encrypt_message():
    return 's' # -- return message but encrypted


@connect.route('/decrypt')
@login_required
def decrypt():
    return 's' # -- message but decrypted


@connect.route('/generate_keys')
@login_required
def generate_public_key():
    key = RSA.generate(2048)
    return 'keys' # -- it will return the key public for exhage and private for decryption


@connect.route('/settings')
@login_required
def settings():
    return render_template('settings.html')

@connect.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')
# -- how i am going to store user settings
# IDEA: make an mysqlite local to store it
# -- local setting will help identofy the user don't add it
