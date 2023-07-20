from flask import Blueprint, request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash
import re
import csv
import uuid
from datetime import datetime
from common.load_file import load_file

from database.repositories.signup_repeository import Signup

bp = Blueprint('user_signup', __name__)

# ✨ db 연결하기
# db = SignUp()
# 1. submit 버튼 눌렀을 때 중복된 아이디 확인
#     select loginid for user where loginid = {inputid}
#     if loginid:
#       error = "중복된 아이디입니다."
# 2. 비밀번호, 비밀번호 확인이 일치하는지 확인
#     elif password1 != password2:
#       error = "비밀번호가 일치하지 않습니다."
# 3. 입력한 이름, 주소가 이상하지 않은지 확인하는 것도 필요
#      고민...
# ✅ 받아온 생년월일 이용해서 Age create 필요!
# 4. 모든 정보가 이상 없으면, 비밀번호 해싱 + uuid 생성
# 5. 해당 정보로 user db에 insert 해주기(튜플로 보내기)
# ✅ 에러 각각!
@bp.route('/user_signup/', methods=['GET', 'POST'])
def user_signup():
    db = Signup()
    # members = load_file("src/member.csv")
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
        birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
        age = current_date.year - birth_date.year
        if current_date.month < birth_date.month:
            age -= 1
        elif current_date.month == birth_date.month and current_date.day < birth_date.day:
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
            return redirect(url_for('login.login'))

        # ❌ csv ver
        # if any(member["Id"] == sign_id for member in members):
        #     error = '중복된 아이디입니다.'
        # elif password1 != password2:
        #     error = '비밀번호가 일치하지 않습니다.'
        # else:
        #     new_member = {"Id": sign_id, "Password": generate_password_hash(password1)}
        #     with open("src/member.csv", "a", encoding="utf-8", newline="") as file:
        #         fieldnames = ["Id", "Password"]
        #         writer = csv.DictWriter(file, fieldnames=fieldnames)
        #         writer.writerow(new_member)
            # return redirect(url_for('login.login'))
    return render_template("auth/user_signup.html", id_error = id_error, password_error = password_error, name_error = name_error, address_error = address_error)