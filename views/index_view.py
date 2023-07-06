from flask import Blueprint, session, redirect, url_for

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    if 'id' in session:
        return redirect(url_for('users.users'))
    else:
        return redirect(url_for('login.login'))