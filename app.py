from flask import Flask
from models.user import User
from database import db
from flask_login import LoginManager
from flask import request
from flask import jsonify

app = Flask(__name__)
app.config['SECRETY_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager() 

db.init_app(app)
login_manager.init_app(app)

@app.rout('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username and password:
        pass

    return jsonify({'message': 'Invalid credentials'}), 400

@app.route('/hello-world', methods=['GET'])
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)