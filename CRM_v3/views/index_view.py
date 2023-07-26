from flask import Blueprint, session, redirect, url_for, render_template, request
import uuid

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    nonuser = request.args.get('nonuser', default="", type=str)
    if nonuser == "nonuser":
        nonuser_uuid = uuid.uuid4()
        return redirect(url_for('select_store.select_store', nonuser_uuid = nonuser_uuid))

    if 'id' in session:
        return redirect(url_for('users.users'))
    else:
        return render_template('index.html')
    