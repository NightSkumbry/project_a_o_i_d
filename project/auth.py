from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Пожалуйста, проверьте введённые данные и попробуйте снова.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    if current_user.register_ended:
        return redirect(url_for('profile.main_profile'))
    else:
        return redirect(url_for('main.end_register'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    family_size = int(request.form.get('family_size').replace('e', ''))
    password = request.form.get('password')
    pets_count = int(request.form.get('pets_count').replace('e', ''))

    if not all([email, family_size > 0, password, pets_count >= 0]): # if a user is found, we want to redirect back to signup page so user can try again
        flash('1Заполните все обязательные поля, пожалуйста')
        return redirect(url_for('auth.signup'))
    # print(f'{email=} {name=} {password=} {second_name=}')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('0Данный адрес электронной почты уже используется.')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email,
                    family_size=family_size,
                    password=generate_password_hash(password, method='sha256'),
                    pets_count=pets_count)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
