from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import db

profile = Blueprint('profile', __name__)


@profile.route('/profile')
@login_required
def main_profile():
    if not current_user.register_ended:
        return redirect(url_for('main.end_register'))

    return render_template('profile.html')

@profile.route('/profile', methods=['POST'])
@login_required
def main_profile_post():
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
    # print([salary, an_income, clothes, food, comunal, other, internet, subscribtions, fun, car, bus, pets])

    if salary == '': salary = current_user.salary
    if an_income == '': an_income = current_user.another_income
    if clothes == '': clothes = current_user.clothes_spend
    if food == '': food = current_user.food_spend
    if comunal == '': comunal = current_user.communal_spend
    if other == '': other = current_user.other_spend
    if internet == '': internet = current_user.internet_spend
    if subscribtions == '': subscribtions = current_user.subscribtions_spend
    if fun == '': fun = current_user.fun_spend
    if car == '': car = current_user.car_spend
    if bus == '': bus = current_user.bus_spend
    if pets == '': pets = current_user.pets_spend

    if not current_user.register_ended:
        return redirect(url_for('main.end_register'))

    current_user.end_registeration(*map(int, [salary, an_income, clothes, food, comunal, other, internet, subscribtions, fun, car, bus, pets]))
    db.session.commit()

    return redirect(url_for('profile.main_profile'))


@profile.route('/credit')
@login_required
def credit():
    if not current_user.register_ended:
        return redirect(url_for('main.end_register'))

    return render_template('credit.html')


@profile.route('/vklad')
@login_required
def vklad():
    if not current_user.register_ended:
        return redirect(url_for('main.end_register'))

    return render_template('vklad.html')
