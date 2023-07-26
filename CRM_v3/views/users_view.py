from flask import Blueprint, request, render_template

from models import User
from repositories.user_repository import UserRepository

bp = Blueprint('users', __name__)

@bp.route('/users/')
def users():
    data_repo = UserRepository()

    page = request.args.get('page', default=1, type=int)
    search_name = request.args.get('name', default="", type=str)
    search_gender = request.args.get('gender', default="", type=str).lower()

    keywords = "&name=" + search_name
    keywords += "&gender=" + search_gender

    search = []
    if search_name:
        search.append(User.name.like(f'%{search_name}%'))
    if search_gender:
        search.append(User.gender == f'{search_gender}')

    if search_name or search_gender:
        total_pages = data_repo.get_total_pages(User, search)
        page_data = data_repo.get_page_data(User, page, search)
    else:
        total_pages = data_repo.get_total_pages(User)
        page_data = data_repo.get_page_data(User, page)

    return render_template("users.html", users = page_data, total_pages = total_pages, current_page = page, keywords = keywords, search_name=search_name, search_gender = search_gender)
