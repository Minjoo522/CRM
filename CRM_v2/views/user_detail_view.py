from flask import Blueprint, render_template
from database.repositories.user_repository import User

bp = Blueprint('user_detail', __name__)

@bp.route('/user_detail/<selected_id>/')
def user_detail(selected_id):
    db = User()
    user = db.searh_by_id('user', selected_id)
    return render_template("user_detail.html", user = user)