from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    family_size = db.Column(db.Integer)
    pets_count = db.Column(db.Integer)

    register_ended = db.Column(db.Boolean)

    salary = db.Column(db.Integer)
    another_income = db.Column(db.Integer)
    clothes_spend = db.Column(db.Integer)
    clothes_spend_good = db.Column(db.Integer)
    food_spend = db.Column(db.Integer)
    food_spend_good = db.Column(db.Integer)
    communal_spend = db.Column(db.Integer)
    other_spend = db.Column(db.Integer)
    mounthly_remains = db.Column(db.Integer)
    mounthly_remains_good = db.Column(db.Integer)
    internet_spend = db.Column(db.Integer)
    subscribtions_spend = db.Column(db.Integer)
    subscribtions_spend_good = db.Column(db.Integer)
    fun_spend = db.Column(db.Integer)
    fun_spend_good = db.Column(db.Integer)
    car_spend = db.Column(db.Integer)
    bus_spend = db.Column(db.Integer)
    bus_spend_good = db.Column(db.Integer)
    pets_spend = db.Column(db.Integer)
    pets_spend_good = db.Column(db.Integer)
    

    def __init__(self, email, password, family_size, pets_count):
        self.email = email
        self.password = password
        self.family_size = family_size
        self.pets_count = pets_count
        self.register_ended = False
        self.salary = 0
        self.another_income = 0
        self.clothes_spend = 0
        self.clothes_spend_good = 0
        self.food_spend = 0
        self.food_spend_good = 0
        self.communal_spend = 0
        self.other_spend = 0
        self.mounthly_remains = 0
        self.mounthly_remains_good = 0
        self.internet_spend = 0
        self.subscribtions_spend = 0
        self.subscribtions_spend_good = 0
        self.fun_spend = 0
        self.fun_spend_good = 0
        self.car_spend = 0
        self.bus_spend = 0
        self.bus_spend_good = 0
        self.pets_spend = 0
        self.pets_spend_good = 0
        

    def end_registeration(self, salary, another_income, clothes_spend, food_spend, communal_spend, other_spend, internet_spend, subscribtions_spend, fun_spend, car_spend, bus_spend, pets_spend):
        self.salary = salary
        self.another_income = another_income

        self.clothes_spend = clothes_spend
        k = 1
        if 35_000 >= clothes_spend/self.family_size > 20_000:
            k = 0.6
        elif clothes_spend/self.family_size > 35_000:
            k = 0.35
        self.clothes_spend_good = int(clothes_spend * k)
        
        self.food_spend = food_spend
        k = 1
        if 20_000 >= food_spend/self.family_size > 10_000:
            k = 0.7
        elif food_spend/self.family_size > 20_000:
            k = 0.3
        self.food_spend_good = int(food_spend * k)
        
        self.communal_spend = communal_spend
        
        self.other_spend = other_spend
        
        self.register_ended = True
        
        self.internet_spend = internet_spend
        
        self.subscribtions_spend = subscribtions_spend
        k = 1
        if 2_000 >= subscribtions_spend/self.family_size > 1_500:
            k = 0.75
        elif subscribtions_spend/self.family_size > 2_000:
            k = 0.25
        self.subscribtions_spend_good = int(subscribtions_spend * k)
        
        self.fun_spend = fun_spend
        k = 1
        if 6_500 >= fun_spend/self.family_size > 3_000:
            k = 0.5
        elif fun_spend/self.family_size > 6_500:
            k = 0.2
        self.fun_spend_good = int(fun_spend * k)
        
        self.car_spend = car_spend
        
        self.bus_spend = bus_spend
        k = 1
        if 4_000 >= bus_spend/self.family_size > 2_500:
            k = 0.7
        elif bus_spend/self.family_size > 4_000:
            k = 0.35
        self.bus_spend_good = int(bus_spend * k)
        
        self.pets_spend = pets_spend
        k = 1
        if 6_000 >= pets_spend/self.pets_count > 4_000:
            k = 0.7
        elif pets_spend/self.pets_count > 6_000:
            k = 0.5
        self.pets_spend_good = int(pets_spend * k)

        self.mounthly_remains = salary + another_income - clothes_spend - food_spend - communal_spend - internet_spend - subscribtions_spend - fun_spend - car_spend - bus_spend - pets_spend - other_spend
        self.mounthly_remains_good = salary + another_income - self.clothes_spend_good - self.food_spend_good - communal_spend - internet_spend - self.subscribtions_spend_good - self.fun_spend_good- car_spend - self.bus_spend_good - self.pets_spend_good - other_spend
