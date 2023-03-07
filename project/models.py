from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    second_name = db.Column(db.String(100))

    register_ended = db.Column(db.Boolean)

    salary = db.Column(db.Integer)
    another_income = db.Column(db.Integer)
    clothes_spend = db.Column(db.Integer)
    food_spend = db.Column(db.Integer)
    communal_spend = db.Column(db.Integer)
    other_spend = db.Column(db.Integer)
    mounthly_remains = db.Column(db.Integer)

    

    def __init__(self, email, password, name, second_name):
        self.email = email
        self.password = password
        self.name = name
        self.second_name = second_name
        self.register_ended = False
        self.salary = 0
        self.another_income = 0
        self.clothes_spend = 0
        self.food_spend = 0
        self.communal_spend = 0
        self.other_spend = 0
        self.mounthly_remains = 0
        

    def end_registeration(self, salary, another_income, clothes_spend, food_spend, communal_spend, other_spend):
        self.salary = salary
        self.another_income = another_income
        self.clothes_spend = clothes_spend
        self.food_spend = food_spend
        self.communal_spend = communal_spend
        self.other_spend = other_spend
        self.mounthly_remains = salary+another_income-clothes_spend-food_spend-communal_spend-other_spend
        self.register_ended = True
