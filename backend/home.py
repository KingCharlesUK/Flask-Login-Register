from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user

from models import db, Users

home = Blueprint('home', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(home)

@home.route('/home', methods=['GET'])
@login_required
def show():
    return render_template('home.html')
