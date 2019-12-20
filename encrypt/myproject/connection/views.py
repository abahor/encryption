import base64
import os
from functools import wraps

import requests
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from flask import redirect, render_template, Blueprint, request, flash, send_from_directory, Markup, url_for, session, \
    abort
from flask_login import login_user, logout_user, current_user
from myproject.connection.form import LoginForm

main = Blueprint('main', __name__, template_folder='temp')

lis = {'id': 0, 'token': 0}
req = requests.Session()
key = RSA.generate(2048)
pri = key.exportKey()
pub = key.publickey().exportKey()


# --- useful functions
def check_logged(f):
    @wraps(f)
    def wra(*args, **kwargs):
        try:
            user = req.post('http://127.0.0.1:5000/if_logged_in')
        except Exception as e:
            return render_template('check_your_network.html', e=e)
        if user.status_code == 200:
            return f(*args, **kwargs)
        else:
            return redirect('/logout')

    return wra


# -- i will need to define a request.Session for the hole routes

# -- there must be a general request method here to handle all the cookies for each app

@main.route('/connect')
@check_logged
def connect():
    return render_template('main.html', token=lis['token'])


@main.route('/got_connected')
@check_logged
def got_connected():
    peer_id = request.args.get('peerid')
    token = request.args.get('token')
    return render_template('chat_tab.html', peer_id=peer_id, token=token)


@main.route('/call')
@check_logged
def call():
    # -- open a conversation (chat) between two people
    return render_template('call.html')


# -- future route call () video() voice() media()

@main.route('/encrypt')
@check_logged
def encrypt_message():
    his_public_key = request.args.get('hiskey')
    message = request.args.get('message')
    encryption_key = RSA.import_key(his_public_key)
    enc = PKCS1_OAEP.new(encryption_key)

    return base64.b64encode(enc.encrypt(message))  # -- return message but encrypted


@main.route('/decrypt')
@check_logged
def decrypt():
    message = request.args.get('message')
    decrypt_key = RSA.import_key(pri)
    # --------------- see if js can hold a key of encryption and decryptio
    decrypt = PKCS1_OAEP.new(decrypt_key)

    return decrypt.decrypt(base64.b64decode(message))  # -- message but decrypted


@main.route('/get_public_key')
@check_logged
def get_public_key():
    return base64.b64encode(pub)  # -- it will return the key public for exhage and private for decryption


@main.route('/settings')
@check_logged
def settings():
    return render_template('settings.html')


@main.route('/logout')
@check_logged
def logout():
    logout_user()
    req.request('GET', 'https://127.0.0.1:5000/logout?id=' + str(lis['id']))
    req.cookies.clear()
    return redirect('/login')


# -- how i am going to store user settings
# IDEA: make an mysqlite local to store it
# -- local setting will help identify the user don't add it

@main.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # req = requests.Session()
        # print(form.email.data)
        paramed = {'c': form.email.data}
        username = req.post('http://127.0.0.1:5000/username', params=paramed)
        if username.status_code == 200:
            params = {'c': form.password.data}
            # -- username stored in the Session['username']
            password = req.post('http://127.0.0.1:5000/password', params=params)
            # -- limiter for the password route in the server
            # print('password')
            if password.status_code == 200:
                # login_user(current_user, remember=True)
                print(password)

                p = password
                o = p.json()
                lis['id'] = o['id']
                lis['token'] = o['token']
                return redirect(url_for('main.connect'))
            else:
                flash(Markup('''<div class="alert alert-danger alert-dismissible fade show" role="alert">Email or Password is wrong 
                </div>'''))
        else:
            flash(Markup('''<div class="alert alert-danger alert-dismissible fade show" role="alert">Email or 
            Password is wrong click here if you forgot your password <a style='' href='http://127.0.0.1:5000/forget-password'>forget password</a></div>'''))  # <a

    return render_template('login.html', form=form)


# @main.route('/logout')
# @check_logged
# def logout():
#     logout_user()
#     redirect('/login')
# @main.route('/favicon.ico')
# def favicon():
#     print('testing')
#     return send_from_directory(os.path.join(main.root_path, 'static'),
#                                'speech-bubble.ico', mimetype='image/vnd.microsoft.icon')

@main.route('/favicon.ico')
def favicon():
    return send_from_directory("static", filename='speech-bubble.png'
                               , mimetype='image/vnd.microsoft.icon')

# @main.route('/send_cookies', methods=['POST','GET'])
# def send_cookies():
#     return req.cookies


# <div>Icons made by <a href="https://www.flaticon.com/authors/chanut" title="Chanut">Chanut</a> from <a
# href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

# @main.route('/send_cookies')
# def send_cookies():
#     return str(req.cookies)
