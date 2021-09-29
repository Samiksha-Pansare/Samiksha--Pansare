# importing libraries
from flask import Flask,redirect,url_for,request,render_template,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import os
from flask import send_from_directory

app = Flask(__name__)

# change to name of your database; add path if necessary
db_name = 'messages.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# NOTHING BELOW THIS LINE NEEDS TO CHANGE
# this route will test the database connection and nothing more
# @app.route('/')
# def testdb():
#     try:
#         db.session.query(text('1')).from_statement(text('SELECT 1')).all()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         # e holds description of the error
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text



class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    email = db.Column(db.String(50))
    subject = db.Column(db.String(15))
    msg = db.Column(db.String(150))
    def __init__(self, name, email, subject, msg):
        self.name = name
        self.email = email
        self.subject = subject
        self.msg = msg



@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']
        print("Inside This Function")
        new_msg = Messages(name=name, email=email, subject=subject, msg=msg)
        db.session.add(new_msg)
        db.session.commit()        
        return render_template('index.html')
    return render_template('index.html')

@app.route("/resume/")
def resume():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/files/'
    return send_from_directory(filepath, 'Samiksha__Pansare.pdf')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
