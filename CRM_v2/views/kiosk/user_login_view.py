from flask import Blueprint, request, redirect, url_for, render_template
from werkzeug.security import check_password_hash

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

        login_user_data = db.get_login_user_data('user', id_)
        hash_password = login_user_data['LoginPassword']
        if login_user_data and check_password_hash(hash_password, password):
            return redirect(url_for('select_store.select_store', user_uuid = login_user_data['Id']))
        error = '아이디와 비밀번호를 확인해주세요.'

    return render_template("auth/user_login.html", error = error)