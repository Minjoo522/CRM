from flask import Blueprint, request, render_template
from db import DbController

bp = Blueprint('users', __name__)

@bp.route('/users/')
def users():
    db_controller = DbController()
    page = request.args.get('page', default=1, type=int)
    search_name = request.args.get('name', default="", type=str)
    search_gender = request.args.get('gender', default="", type=str)
    users = db_controller.get_info('user')

    data = []
    page_data = []

    for user in users:
        if search_name in user['Name']:
            if search_gender in user['Gender']:
                data.append(user)
    
    keywords = "&name=" + search_name
    keywords += "&gender=" + search_gender

    total_pages = db_controller.get_count('user')
    # start_index = Pagination().get_start_index(page)
    # end_index = Pagination().get_end_index(start_index)
    # page_data = data[start_index:end_index] # 페이지 정보 받아오기
    page_data = db_controller.page_item('user', page)
    return render_template("users.html", users = page_data, total_pages = total_pages, current_page = page, keywords = keywords, search_name=search_name, search_gender = search_gender)
