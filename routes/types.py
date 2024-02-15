from flask import Blueprint, app, render_template, request
import connection

types = Blueprint("types", __name__, static_folder="static", template_folder="templates")

@types.route('/types', methods=['GET', 'POST'])
def aircraft_type():
    types = connection.fetch_all_aircraft_types()
    print(types)
    return render_template("aircraft-type.html", types=types)

@types.route('/create-types', methods=['GET', 'POST'])
def create_types():
    if request.method == "POST":
        connection.create_types(request.form)
        return "success"
    return render_template("create-types.html")

@types.route('/edit-types/<types_id>', methods=['GET', 'POST'])
def edit_types(types_id=0):
    types_id = 1
    if request.method == "POST":
        connection.edit_types(request.form, types_id)
        return "success"
    return render_template("edit-types.html", types=types_id)