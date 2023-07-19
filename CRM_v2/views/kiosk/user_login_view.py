from flask import Blueprint, request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash

# db
from database.repositories.login_repository import Login

bp = Blueprint('user_login', __name__)

@bp.route('/user_login/', methods=['GET', 'POST'])
def user_login():
    db = Login()

    error = None
    if request.method == 'POST':
        id_ = request.form['user-login-id']
        password = request.form['user-login-password']
        hash_password = generate_password_hash(password)

        login_user_data = db.get_login_user_data('user', id_, hash_password)
        if login_user_data:
            return redirect(url_for('new_order.new_order', user_uuid = login_user_data['Id']))
        error = '존재하지 않는 회원입니다.'

    return render_template("auth/user_login.html", error = error)