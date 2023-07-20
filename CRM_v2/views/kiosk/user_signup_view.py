from flask import Blueprint, request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash
import csv
import uuid
from common.load_file import load_file

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
@bp.route('/user_signup/', methods=['GET', 'POST'])
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
    return render_template("auth/user_signup.html", error = error)