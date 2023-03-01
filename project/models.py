from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    second_name = db.Column(db.String(100))
    father_name = db.Column(db.String(100))
    birthday = db.Column(db.DateTime)
    sex = db.Column(db.Integer)

    def __init__(self, email, password, name, second_name, birthday):
        self.email = email
        self.password = password
        self.name = name
        self.second_name = second_name
        self.birthday = birthday

        self.father_name = ''
        self.sex = 0

    def set_fathername(self, father_name):
        self.father_name = father_name

    def set_sex(self, sex):
        self.sex = sex
