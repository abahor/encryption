from flask import redirect, render_template, Blueprint, url_for, session, request, flash, abort
from myproject.connection.form import LoginForm
from flask_login import login_required, login_user, logout_user, current_user
import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

connect = Blueprint('connect', __name__, template_folder='temp')

lis = {'id': 0, 'token': 0}
req = requests.Session()
key = RSA.generate(2048)
pri = t.exportKey()
pub = t.publickey().exportKey()


# -- i will need to define a request.Session for the hole routes

# -- there must be a general request method here to handle all the cookies for each app

@connect.route('/connect')
@login_required
def connect():
    return render_template('main.html', token=lis['token'])


@connect.route('/got_connected')
@login_required
def got_connected():
    peer_id = request.args.get('peerid')
    token = request.args.get('token')
    return render_template('chat_tab.html', peer_id=peer_id, token=token)


@connect.route('/call')
@login_required
def call():
    # -- open a conversation (chat) between two people
    return render_template('call.html')


# -- future route call () video() voice() media()

@connect.route('/encrypt')
@login_required
def encrypt_message():
    his_public_key = request.args.get('hiskey')
    message = request.args.get('message')
    encryption_key = RSA.import_key(his_public_key)
    enc = PKCS1_OAEP.new(his_public_key)

    return base64.b64encode(enc.encrypt(message))  # -- return message but encrypted


@connect.route('/decrypt')
@login_required
def decrypt():
    message = request.args.get('message')
    decrypt_key = RSA.import_key(pri)
    # --------------- see if js can hold a key of encryption and decryptio
    decrypt = PKCS1_OAEP.new(decrypt_key)

    return decrypt.decrypt(base64.b64decode(message))  # -- message but decrypted


@connect.route('/get_public_key')
@login_required
def get_public_key():
    return base64.b64encode(pub)  # -- it will return the key public for exhage and private for decryption


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

@connect.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # req = requests.Session()
        paramed = {'c': form.email.data}
        username = req.post('http://127.0.0.1:5000/username', params=paramed)
        if username.status_code == 200:
            params = {'c': form.password.data}
            # -- username stored in the Session['username']
            password = req.post('http://127.0.0.1:5000/password', params=params)
            # -- limiter for the password route in the server
            if password.status_code == 200:
                login_user(current_user)
                lis['id'] = password.text.split('0')
                lis['token'] = password.text.split('1')
                redirect('/connect')
        else:
            flash("email or password isn't correct")
    return render_template('login.html', form=form)


@connect.route('/logout')
@login_required
def logout():
    logout_user()
    redirect('/login')
