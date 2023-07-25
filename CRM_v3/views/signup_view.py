from flask import Blueprint, request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash

from database.repositories.signup_repeository import Signup

bp = Blueprint('signup', __name__)

@bp.route('/signup/', methods=['GET', 'POST'])
def signup():
    db = Signup()

    error = None
    if request.method == 'POST':
        sign_id = request.form['sign_id']
        password1 = request.form['password1']
        password2 = request.form['password2']
        hash_password = generate_password_hash(password1)

        check_id_existence = db.check_id_existence('admin', sign_id)
        if check_id_existence:
            error = '중복된 아이디입니다.'
        elif password1 != password2:
            error = '비밀번호가 일치하지 않습니다.'
        else:
            db.insert_admin_signup_data(sign_id, hash_password)
            return redirect(url_for('login.login'))

    return render_template("auth/signup.html", error = error)