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
    return render_template("admin/airports.html", airports=airports_dict)

def list_single_airport():
    pass

def edit_airport():
    pass

@admin.route('/airports/create', methods=['GET', 'POST'])
def create_airport():
    return render_template("admin/airports/create.html")