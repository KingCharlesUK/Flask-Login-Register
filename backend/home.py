from flask import Blueprint, render_template

home = Blueprint('home', __name__, template_folder='../frontend')

@home.route('/home', methods=['GET'])
def show():
    return render_template('home.html')