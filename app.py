from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import csv
import os

from pagination import Pagination

app = Flask(__name__)
app.secret_key = os.urandom(24)

def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data_list = []
        datas = csv.DictReader(file, skipinitialspace=True)
        for data in datas:
            data_list.append(data)
    return data_list

@app.route('/')
def index():
    if 'id' in session:
        return redirect(url_for('users'))
    else:
        return redirect(url_for('login'))

# Log in
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        members = load_file("src/member.csv")
        id_ = request.form['id']
        password = request.form['password']

        for member in members:
            if id_ == member["Id"]:
                print(id_, member["Id"])
                stored_password = member["Password"]
                if check_password_hash(stored_password, password):
                    session['id'] = id_
                    return redirect(url_for('users'))
                else:
                    error = '비밀번호가 틀렸습니다.'
                    break
            error = '존재하지 않는 회원입니다.'

    return render_template("auth/login.html", error = error)

# Log out
@app.route('/logout')
def logout():
    session.pop('id', None)

# Signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    members = load_file("src/member.csv")
    error = None
    if request.method == 'POST':
        sign_id = request.form['sign_id']
        password1 = request.form['password1']
        password2 = request.form['password2']

        if any(member["Id"] == sign_id for member in members):
            error = '아이디 중복'
        elif password1 != password2:
            error = '비밀번호가 일치하지 않습니다.'
        else:
            new_member = {"Id": sign_id, "Password": generate_password_hash(password1)}
            with open("src/member.csv", "a", encoding="utf-8", newline="") as file:
                fieldnames = ["Id", "Password"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(new_member)
            return redirect(url_for('login'))
    return render_template("auth/signup.html", error = error)

@app.route('/users')
def users():
    page = request.args.get('page', default=1, type=int)
    search_name = request.args.get('name', default="", type=str)
    search_gender = request.args.get('gender', default="", type=str)
    users = load_file("src/user.csv")

    data = []
    page_data = []

    for user in users:
        if search_name in user['Name']:
            if search_gender in user['Gender']:
                data.append(user)
    
    keywords = ""
    keywords += "&name=" + search_name
    keywords += "&gender=" + search_gender

    total_pages = Pagination().get_total_pages(data)
    start_index = Pagination().get_start_index(page)
    end_index = Pagination().get_end_index(start_index)
    page_data = data[start_index:end_index]
    return render_template("users.html", users = page_data, total_pages = total_pages, current_page = page, keywords = keywords, search_name=search_name)

@app.route('/user_detail/<selected_id>')
def user_detail(selected_id):
    users = load_file("src/user.csv")
    for user in users:
        if user['Id'] == selected_id:
            return render_template("user_detail.html", user = user)

@app.route('/stores')
def stores():
    page = request.args.get('page', default=1, type=int)
    search_store_name = request.args.get('store-name', default="", type=str)
    stores = load_file("src/store.csv")

    data = []
    page_data = []

    for store in stores:
        if search_store_name in store['Name']:
            data.append(store)

    keywords = ""
    keywords += "&store-name=" + search_store_name

    total_pages = Pagination().get_total_pages(data)
    start_index = Pagination().get_start_index(page)
    end_index = Pagination().get_end_index(start_index)
    page_data = data[start_index:end_index]
    return render_template("stores.html", stores = page_data, total_pages = total_pages, current_page = page, keywords = keywords, search_store_name = search_store_name)

@app.route('/store_detail/<selected_id>')
def store_detail(selected_id):
    stores = load_file("src/store.csv")
    for store in stores:
        if store['Id'] == selected_id:
            return render_template("store_detail.html", store = store)

@app.route('/items')
def items():
    page = request.args.get('page', default=1, type=int)
    search_type = request.args.get('type', default="", type=str)
    items = load_file("src/item.csv")

    data = []
    page_data = []

    # 아이템 타입 분류
    item_type = { item['Type'] for item in items }
    
    for item in items:
        if search_type in item['Type']:
            data.append(item)

    keywords = ""
    keywords += "&type=" + search_type

    total_pages = Pagination().get_total_pages(data)
    start_index = Pagination().get_start_index(page)
    end_index = Pagination().get_end_index(start_index)
    page_data = data[start_index:end_index]
    return render_template("items.html", items = page_data, total_pages = total_pages, current_page = page, item_type = item_type, keywords=keywords)
    
@app.route('/item_detail/<selected_id>')
def item_detail(selected_id):
    items = load_file("src/item.csv")
    for item in items:
        if item['Id'] == selected_id:
            return render_template("item_detail.html", item = item)
            
@app.route('/orders')
def orders():
    page = request.args.get('page', default=1, type=int)
    orders = load_file("src/order.csv")

    data = []
    page_data = []
    
    for order in orders:
        data.append(order)

    total_pages = Pagination().get_total_pages(data)
    start_index = Pagination().get_start_index(page)
    end_index = Pagination().get_end_index(start_index)
    page_data = data[start_index:end_index]
    return render_template("orders.html", orders = page_data, total_pages = total_pages, current_page = page)
    
# orderitem_detail
# @app.route('/orderitem_detail')

@app.route('/order_items')
def order_items():
    page = request.args.get('page', default=1, type=int)
    order_items = load_file("src/orderitem.csv")

    data = []
    page_data = []
    
    for order_item in order_items:
        data.append(order_item)

    total_pages = Pagination().get_total_pages(data)
    start_index = Pagination().get_start_index(page)
    end_index = Pagination().get_end_index(start_index)
    page_data = data[start_index:end_index]
    return render_template("order_items.html", order_items = page_data, total_pages = total_pages, current_page = page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="8001")