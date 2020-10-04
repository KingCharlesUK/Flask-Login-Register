from flask import Blueprint, url_for, redirect
from flask_login import LoginManager, login_required, logout_user

logout = Blueprint('logout', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(logout)

@logout.route('/logout')
@login_required
def show():
    logout_user()
    return redirect(url_for('login.show') + '?success=logged-out')