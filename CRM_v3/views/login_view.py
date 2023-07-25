from flask import Blueprint, request, redirect, url_for, render_template
from werkzeug.security import check_password_hash

# db
from database.repositories.login_repository import Login

bp = Blueprint('login', __name__)

@bp.route('/login/', methods=['GET', 'POST'])
def login():
    db = Login()

    error = None
    if request.method == 'POST':
        id_ = request.form['id']
        password = request.form['password']

        login_user_data = db.get_login_user_data('admin', id_)
        hash_password = login_user_data['LoginPassword']
        if login_user_data and check_password_hash(hash_password, password):
            return redirect(url_for('users.users'))
        error = '아이디와 비밀번호를 확인해주세요.'

    return render_template("auth/login.html", error = error)
