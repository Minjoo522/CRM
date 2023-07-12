from flask import Blueprint, request, render_template
from common.load_file import load_file
from common.pagination import Pagination
from db import get_info

bp = Blueprint('users', __name__)

@bp.route('/users/')
def users():
    page = request.args.get('page', default=1, type=int)
    search_name = request.args.get('name', default="", type=str)
    search_gender = request.args.get('gender', default="", type=str)
    users = get_info()

    data = []
    page_data = []

    for user in users:
        if search_name in user['Name']:
            if search_gender in user['Gender']:
                data.append(user)
    
    keywords = "&name=" + search_name
    keywords += "&gender=" + search_gender

    total_pages = Pagination().get_total_pages(data)
    start_index = Pagination().get_start_index(page)
    end_index = Pagination().get_end_index(start_index)
    page_data = data[start_index:end_index]
    return render_template("users.html", users = page_data, total_pages = total_pages, current_page = page, keywords = keywords, search_name=search_name, search_gender = search_gender)
