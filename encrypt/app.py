import os

# from flask import send_from_directory, send_file
from myproject import app
# import pyfladesk

# @app.route('/favicon.ico')
# def favicon():
#     print('testing')
#     return send_file('static', 'speed-bubble.ico')


if __name__ == '__main__':
    # pyfladesk.init_gui(app, window_title='Chat app', icon=os.getcwd() + "/myproject/static/speech-bubble.png")
    app.run(debug=True, port=5050)
