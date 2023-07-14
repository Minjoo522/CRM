from flask import Blueprint, request, render_template
from database.repositories.user_repository import User

bp = Blueprint('users', __name__)

@bp.route('/users/')
def users():
    db = User()

    page = request.args.get('page', default=1, type=int)
    search_name = request.args.get('name', default="", type=str)
    search_gender = request.args.get('gender', default="", type=str)

    keywords = "&name=" + search_name
    keywords += "&gender=" + search_gender

    if search_name or search_gender:
        total_pages = db.get_search_total_pages('user', search_name, search_gender)
        page_data = db.get_search_data('user', search_name, search_gender, page)
    else:
        total_pages = db.get_total_pages('user')
        page_data = db.get_page_item('user', page)

    return render_template("users.html", users = page_data, total_pages = total_pages, current_page = page, keywords = keywords, search_name=search_name, search_gender = search_gender)
