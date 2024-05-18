from flask import Blueprint, app, redirect, render_template, request
from classes.db import DbQuery
import connection
from classes.routes import Routes

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates/admin")
db = DbQuery()

@admin.route('/', methods=['GET', 'POST'])
def dashboard():
    return render_template("admin/dashboard.html")

# authentication pages
@admin.route('/login', methods=['GET', 'POST'])
def login_page():
    return render_template("admin/auth/login.html")

@admin.route('/register', methods=['GET', 'POST'])
def register_page():
    return render_template("admin/auth/register.html")

# users
@admin.route('/users', methods=['GET', 'POST'])
def list_all_users():
    return render_template("admin/users.html")

def list_single_user():
    pass

def edit_user():
    pass

def create_user():
    pass

# routes
def list_all_routes():
    pass

def list_single_route():
    pass

def edit_route():
    pass

def create_route():
    pass


# airports
@admin.route('/airports', methods=['GET', 'POST'])
def list_all_airports():
    airports_list = db.select_all_from("airports")
    airports_dict = []
    for row in airports_list:
        row_as_dict = row._mapping
        airports_dict.append(row_as_dict)
    return render_template("admin/airports/list.html", airports=airports_dict)

def list_single_airport():
    pass

@admin.route("/airports/edit/<airport_id>", methods=['GET', 'POST'])
def edit_airport(airport_id=0):
    if request.method == 'POST':
        db.update_where('airports', request.form, airport_id)
        return redirect("/admin/airports")
    res = db.select_all_from_where_id('airports', airport_id)
    dict = []
    for row in res:
        row_as_dict = row._mapping
        dict.append(row_as_dict)
    return render_template("admin/airports/edit.html", airport=dict)

@admin.route('/airports/create', methods=['GET', 'POST'])
def create_airport():
    if request.method == 'POST':
        db.insert_into('airports', request.form)
        return redirect("/admin/airports")
    return render_template("admin/airports/edit.html", airport=dict)

@admin.route('/airports/delete/<airport_id>', methods=['POST'])
def delete_airport(airport_id=0):
    db.delete_where('airports', airport_id)
    return redirect("/admin/airports")
    


# airframes
@admin.route('/airframes/list', methods=['GET', 'POST'])
def list_all_airframes():
    query = "SELECT * FROM airframes a RIGHT JOIN aircraft_type at on a.id_aircraft_type = at.id"
    airframe_list = db.specific_query(query, True)
    airframes_dict = []
    for row in airframe_list:
        row_as_dict = row._mapping
        airframes_dict.append(row_as_dict)
    return render_template("admin/airframes/list.html", airframes=airframes_dict)

@admin.route('/airframes/create', methods=['GET', 'POST'])
def create_airframe():
    if request.method == "POST":
        db.insert_into("airframes", request.form)
        return "success"
    return render_template("create-airframe.html")

@admin.route('/airframes/edit/<airframe_id>', methods=['GET', 'POST'])
def edit_airframe(airframe_id=0):
    if request.method == "POST":
        db.update_where("airframes", request.form, airframe_id)
        return "success"
    return render_template("edit-airframe.html", airframe=airframe_id)

@admin.route('airframes/delete/<airframe_id>', methods=['POST'])
def delete_airframe(airframe_id=0):
    if request.method == "POST":
        db.delete_where("airframes", airframe_id)
        return redirect(list_all_airframes())

# types
@admin.route('/types/list', methods=['GET', 'POST'])
def list_all_aircraft_types():
    types = db.select_all_from("types")
    return render_template("admin/types/list.html", types=types)

@admin.route('/create-types', methods=['GET', 'POST'])
def create_type():
    if request.method == "POST":
        db.insert_into("types", request.form)
        return "success"
    return render_template("create-types.html")

@admin.route('/types/edit/<types_id>', methods=['GET', 'POST'])
def edit_type(types_id=0):
    types = db.select_all_from_where_id("types", types_id)
    if request.method == "POST":
        db.update_where("types", request.form, types_id)
        return redirect(list_all_aircraft_types())
    return render_template("admin/types/edit.html", types=types)

@admin.route('types/delete/<types_id>', methods=['POST'])
def delete_type(types_id=0):
    if request.method == "POST":
        db.delete_where("types", types_id)
        return redirect(list_all_aircraft_types())
    
#routes
@admin.route('routes/list', methods=['GET'])
def list_all_routes():
    routes = Routes().get_all_routes()
    return render_template("admin/routes/list.html", routes=routes)

@admin.route('routes/<id_route>', methods=['GET'])
def info_route(id_route=0):
    routes = Routes().get_single_route(id_route)
    print(routes)
    return render_template("admin/routes/info.html", route=routes[0])