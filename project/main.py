from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@main.route('/profile', methods=['POST'])
@login_required
def profile_score():
    salary = int(request.form.get('salary'))
    an_income = int(request.form.get('an_income'))
    clothes = int(request.form.get('clothes'))
    food = int(request.form.get('food'))
    comunal = int(request.form.get('comunal'))
    other = int(request.form.get('other'))

    a = salary+an_income-clothes-food-comunal-other
    if a > 0:
        flash(f'Сумма ежемесячных накоплений составляет {a} руб.')
    else:
        flash(f'Что бы иметь возможность откладывать хотя бы 1 рубль с текущим доходом, необходимо сократить расходы хотя бы на {1-a} руб.')
    return redirect(url_for('main.profile'))
