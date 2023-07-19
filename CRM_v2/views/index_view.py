from flask import Blueprint, session, redirect, url_for, render_template, request
import uuid

bp = Blueprint('index', __name__)

# TODO: 관리자 아이디 세션에 있는 경우 : 관리자 페이지로
# TODO: 고객 아이디 세션에 있는 경우 : 오더 페이지로
@bp.route('/')
def index():
    nonuser = request.args.get('nonuser', default="", type=str)
    if nonuser == "nonuser":
        nonuser_uuid = uuid.uuid4()
        return redirect(url_for('new_order.new_order', nonuser_uuid = nonuser_uuid))

    if 'id' in session:
        return redirect(url_for('users.users'))
    else:
        return render_template('index.html')
    