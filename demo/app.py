from flask import Flask, request, session, redirect, url_for, abort, render_template, flash
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy

# Create application instance
app = Flask(__name__)
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/test' 

# Create api instance
api = Api(app)

# Create Database instance 
# TODO: check if new instance is needed for different requests
db  = SQLAlchemy(app)

########################################################################
# Webpages
########################################################################

@app.route("/")
def show_entries():
    return render_template('index.html',error='')


########################################################################
# Database Models
########################################################################


class Student(db.Model):
    rollno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    grade = db.Column(db.String(64), nullable=False)

    def __init__(self, rollno, name, grade=''):
        self.rollno = rollno
        self.name = name
        self.grade = grade

    # to get serialized data
    def to_dict(self):
        ret = {c.name: getattr(self, c.name) for c in  self.__table__.columns}
        return ret

########################################################################
# API
########################################################################

class Student_Endpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rollno')
        rollno = parser.parse_args()['rollno']

        return Student.query.filter_by(rollno = rollno).first().to_dict()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rollno')
        parser.add_argument('name')

        name = parser.parse_args()['name']
        rollno = parser.parse_args()['rollno']

        student = Student(rollno, name)
        db.session.add(student)
        db.session.commit()

    def put(self):
        pass

    def patch(self):
        pass
        
    def delete(self):
        pass

api.add_resource(Student_Endpoint, '/student')
