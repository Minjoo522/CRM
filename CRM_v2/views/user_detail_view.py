from flask import Blueprint, render_template
from db import DbController

bp = Blueprint('user_detail', __name__)

@bp.route('/user_detail/<selected_id>/')
def user_detail(selected_id):
    db_controller = DbController()
    user = db_controller.searh_id('user', selected_id)
    return render_template("user_detail.html", user = user)