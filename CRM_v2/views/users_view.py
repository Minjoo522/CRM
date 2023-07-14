from flask import Blueprint, request, render_template
from db import DbController
from database.repositories.user_repository import User
from database.repositories.common.pagination import Pagination

bp = Blueprint('users', __name__)

@bp.route('/users/')
def users():
    db = User()
    db_controller = DbController()
    pagination = Pagination()

    page = request.args.get('page', default=1, type=int)
    search_name = request.args.get('name', default="", type=str)
    search_gender = request.args.get('gender', default="", type=str)

    keywords = "&name=" + search_name
    keywords += "&gender=" + search_gender

    if search_name or search_gender:
        # 페이징 처리 해주어야함 - 카운트
        total_pages = db_controller.get_search_total_pages('user', search_name, search_gender)
        page_data = db_controller.search_name_gender('user', search_name, search_gender, page)
    else:
        total_pages = pagination.get_total_pages('user')
        page_data = pagination.get_page_item('user', page)

    return render_template("users.html", users = page_data, total_pages = total_pages, current_page = page, keywords = keywords, search_name=search_name, search_gender = search_gender)
