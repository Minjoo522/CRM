from flask import Blueprint, request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash
import csv
from load_file import load_file

bp = Blueprint('signup', __name__)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    members = load_file("src/member.csv")
    error = None
    if request.method == 'POST':
        sign_id = request.form['sign_id']
        password1 = request.form['password1']
        password2 = request.form['password2']

        if any(member["Id"] == sign_id for member in members):
            error = '중복된 아이디입니다.'
        elif password1 != password2:
            error = '비밀번호가 일치하지 않습니다.'
        else:
            new_member = {"Id": sign_id, "Password": generate_password_hash(password1)}
            with open("src/member.csv", "a", encoding="utf-8", newline="") as file:
                fieldnames = ["Id", "Password"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(new_member)
            return redirect(url_for('login.login'))
    return render_template("auth/signup.html", error = error)