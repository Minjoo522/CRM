from flask import Blueprint, request, render_template
from database.repositories.user_repository import User

from model.models import UserDb

bp = Blueprint('users', __name__)

@bp.route('/users/')
def users():
    db = User()

    page = request.args.get('page', default=1, type=int)
    search_name = request.args.get('name', default="", type=str)
    search_gender = request.args.get('gender', default="", type=str).lower()

    keywords = "&name=" + search_name
    keywords += "&gender=" + search_gender

    if search_name or search_gender:
        page_data, total_pages = db.get_search_result('user', page, search_name, search_gender)
    else:
        total_pages = db.get_total_pages('user')
        page_data = db.get_page_item('user', page)

    return render_template("users.html", users = page_data, total_pages = total_pages, current_page = page, keywords = keywords, search_name=search_name, search_gender = search_gender)
