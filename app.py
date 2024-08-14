from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'dqllite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'


db = SQLAlchemy(app)


class User(db.model,  UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(80), nullable = False)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__  == "__main__":
    app.run(debug=True)
