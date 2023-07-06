from flask import Blueprint, render_template
from load_file import load_file

bp = Blueprint('user_detail', __name__)

@bp.route('/user_detail/<selected_id>/')
def user_detail(selected_id):
    users = load_file("src/user.csv")
    for user in users:
        if user['Id'] == selected_id:
            return render_template("user_detail.html", user = user)