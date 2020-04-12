from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from models import User
from models import db
from flask_sqlalchemy import SQLAlchemy
import os
import names


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    print('adfadf')
    if request.method == 'POST' and request.form['submit_button']:
        username = request.form['fullname'] 
        print("sadlkfjasdflk " + username)
    users = User.query.all()
    return render_template('display.html',users= users)

@app.route("/search")
def search(name):
    username = request.args.get('name')
    print(username)



def init_db():
    db.drop_all()
    print("[DEBUG] Creating Databases")
    db.create_all()
    for i in range(1, 14):
        name = names.get_full_name()
        user = User(fullname=name)
        db.session.add(user)
        db.session.commit()
    print("[DEBUG] Databases created")
    db.session.commit()


init_db()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()
