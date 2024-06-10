from flask import Blueprint, app, redirect, render_template, request, session
import connection
from classes.users import Users

front = Blueprint("front", __name__, static_folder="static", template_folder="templates/front")

@front.route('/')
@front.route('/home')
def home():
    # dp = Dispatch()
    # dp.request_latest_ofp("")
    return render_template("front/home.html")

@front.route('/fleet')
def fleet():
    res = connection.fetch_all_airframes()
    airframes_dict = []
    for row in res:
        row_as_dict = row._mapping
        airframes_dict.append(row_as_dict)
    unique_types = set()
    for dic in airframes_dict:
        unique_types.add((dic['name'] , dic['id']))
            
    return render_template("front/fleet.html", unique_types=unique_types)

@front.route('/dispatch')
def dispatch():
    pass

@front.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        Users().create_user(request.form)
        return redirect("/")
    return render_template("front/register.html")

@front.route('/login', methods=['POST', "GET"])
def login():
    if request.method == 'POST':
        login = Users().login(request.form['username'], request.form['password'])
        return redirect('/')
    return render_template('front/login.html')

@front.route('/logout', methods=['POST', 'GET'])
def logout():
    Users().logout()
    return redirect('/')