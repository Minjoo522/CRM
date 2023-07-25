from flask import Blueprint, request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash
import re
import uuid
from datetime import datetime

from database.repositories.signup_repeository import Signup

bp = Blueprint('user_signup', __name__)

@bp.route('/user_signup/', methods=['GET', 'POST'])
def user_signup():
    db = Signup()
    id_error = None
    password_error = None
    name_error = None
    address_error = None

    if request.method == 'POST':
        sign_id = request.form['user_sign_id']
        password1 = request.form['user_password1']
        password2 = request.form['user_password2']
        hash_password = generate_password_hash(password1)
        name = request.form['user_name']
        gender = request.form['user_gender']
        birthdate = request.form['user_birthdate']
        address = request.form['user_address']

        name_pattern = re.compile(r'^[가-힣]+$')
        name_min_length = 2
        name_max_length = 10

        current_date = datetime.now()
        birth_date = birthdate.split('-')
        age = current_date.year - int(birth_date[0])
        if current_date.month < int(birth_date[1]):
            age -= 1
        elif current_date.month == int(birth_date[1]) and current_date.day < int(birth_date[2]):
            age -= 1

        address_pattern = re.compile(r'^[가-힣\d\s]+$')

        user_id = str(uuid.uuid4())

        check_id_exsitence = db.check_id_existence('user', sign_id)
        if check_id_exsitence:
            id_error = '중복된 아이디입니다.'
        elif password1 != password2:
            password_error = '비밀번호가 일치하지 않습니다.'
        elif not name_min_length <= len(name) <= name_max_length:
            name_error = '2글자 이상 10글자 이하의 이름을 입력해주세요.'
        elif not re.match(name_pattern, name):
            name_error = '이름은 한글로만 입력할 수 있습니다.'
        elif not re.match(address_pattern, address):
            address_error = '올바르지 않은 주소입니다.'
        else:
            db.insert_user_signup_data(user_id, name, gender, birthdate, age, address, sign_id, hash_password)
            return redirect(url_for('user_login.user_login'))

    return render_template("auth/user_signup.html", id_error = id_error, password_error = password_error, name_error = name_error, address_error = address_error)