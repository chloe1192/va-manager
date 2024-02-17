from flask import Blueprint, app, redirect, render_template, request
import connection

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates/admin")

@admin.route('/', methods=['GET', 'POST'])
def dashboard():
    return render_template("admin/dashboard.html")

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
    airports_list = connection.select_all_from("airports")
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
        connection.update_where('airports', request.form, airport_id)
        return redirect("/admin/airports")
    res = connection.select_all_from_where_id('airports', airport_id)
    dict = []
    for row in res:
        row_as_dict = row._mapping
        dict.append(row_as_dict)
    return render_template("admin/airports/edit.html", airport=dict)

@admin.route('/airports/create', methods=['GET', 'POST'])
def create_airport():
    if request.method == 'POST':
        connection.insert_into('airports', request.form)
        return redirect("/admin/airports")
    return render_template("admin/airports/edit.html", airport=dict)

@admin.route('/airports/delete/<airport_id>', methods=['POST'])
def delete_airport(airport_id=0):
    connection.delete_where('airports', airport_id)
    return redirect("/admin/airports")
    


# airframes
@admin.route('/airframes/list', methods=['GET', 'POST'])
def list_all_airframes():
    airframe_list = connection.fetch_all_airframes()
    airframes_dict = []
    for row in airframe_list:
        row_as_dict = row._mapping
        airframes_dict.append(row_as_dict)
    print(airframes_dict)
    return render_template("admin/airframes/list.html", airframes=airframes_dict)

@admin.route('/airframes/create', methods=['GET', 'POST'])
def create_airframe():
    if request.method == "POST":
        connection.create_airframe(request.form)
        return "success"
    return render_template("create-airframe.html")

@admin.route('/airframes/edit/<airframe_id>', methods=['GET', 'POST'])
def edit_airframe(airframe_id=0):
    if request.method == "POST":
        connection.edit_airframe(request.form, airframe_id)
        return "success"
    return render_template("edit-airframe.html", airframe=airframe_id)

@admin.route('airframes/delete/<airframe_id>', methods=['POST'])
def delete_airframe(airframe_id=0):
    if request.method == "POST":
        connection.delete_airframe(airframe_id)
        return redirect(list_all_airframes())

# types
@admin.route('/types/list', methods=['GET', 'POST'])
def aircraft_type():
    types = connection.fetch_all_aircraft_types()
    print(types)
    return render_template("aircraft-type.html", types=types)

@admin.route('/create-types', methods=['GET', 'POST'])
def create_types():
    if request.method == "POST":
        connection.create_types(request.form)
        return "success"
    return render_template("create-types.html")

@admin.route('/edit-types/<types_id>', methods=['GET', 'POST'])
def edit_types(types_id=0):
    types_id = 1
    if request.method == "POST":
        connection.edit_types(request.form, types_id)
        return "success"
    return render_template("edit-types.html", types=types_id)