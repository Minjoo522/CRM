from flask import Blueprint, request, session, redirect, url_for, render_template
from werkzeug.security import check_password_hash
from load_file import load_file

bp = Blueprint('login', __name__)

@bp.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        members = load_file("src/member.csv")
        id_ = request.form['id']
        password = request.form['password']

        for member in members:
            if id_ == member["Id"]:
                print(id_, member["Id"])
                stored_password = member["Password"]
                if check_password_hash(stored_password, password):
                    session['id'] = id_
                    return redirect(url_for('users.users'))
                else:
                    error = '비밀번호가 틀렸습니다.'
                    break
            error = '존재하지 않는 회원입니다.'

    return render_template("auth/login.html", error = error)