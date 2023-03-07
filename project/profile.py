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


