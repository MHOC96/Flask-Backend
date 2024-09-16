from flask import Flask
from flask_cors import CORS
from register import registration
from login import login

app = Flask(__name__)
CORS(app)

@app.route('/register',methods=["post"])
def register_user():
    return registration()

@app.route('/login',methods=["post"])
def login_user():
    return login()

if __name__ == '__main__':
    app.run(debug=True)