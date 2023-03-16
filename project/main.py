from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/end_register')
@login_required
def end_register():
    return render_template('register_complition.html')

@main.route('/end_register', methods=['POST'])
@login_required
def end_register_post():
    salary = request.form.get('salary')
    an_income = request.form.get('an_income')
    clothes = request.form.get('clothes')
    food = request.form.get('food')
    comunal = request.form.get('comunal')
    other = request.form.get('other')
    internet = request.form.get('internet')
    subscribtions = request.form.get('subscribtions')
    fun = request.form.get('fun')
    car = request.form.get('car')
    bus = request.form.get('bus')
    pets = request.form.get('pets')

    # print([salary, an_income, clothes, food, comunal, other])

    if not all([salary, an_income, clothes, food, comunal, other, internet, subscribtions, fun, car, bus, pets]):
        flash('Вам стоило бы заполнить все поля, хотя бы нулями')
        return redirect(url_for('main.end_register'))

    current_user.end_registeration(*map(int, [salary, an_income, clothes, food, comunal, other, internet, subscribtions, fun, car, bus, pets]))

    db.session.commit()
    return redirect(url_for('profile.main_profile'))
