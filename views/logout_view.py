from flask import Blueprint, session

bp = Blueprint('logout', __name__)

@bp.route('/logout')
def logout():
    session.pop('id', None)