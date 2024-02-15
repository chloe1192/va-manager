from flask import Blueprint, app, redirect, render_template, request
import connection

airframes = Blueprint("airframes", __name__, static_folder="static", template_folder="templates")

@airframes.route('/airframes', methods=['GET', 'POST'])
def list_airframe():
    airframe_list = connection.fetch_all_airframes()
    airframes_dict = []
    for row in airframe_list:
        row_as_dict = row._mapping
        airframes_dict.append(row_as_dict)
    return render_template("airframes.html", airframes=airframes_dict)

@airframes.route('/create-airframe', methods=['GET', 'POST'])
def create_airframe():
    if request.method == "POST":
        connection.create_airframe(request.form)
        return "success"
    return render_template("create-airframe.html")

@airframes.route('/edit-airframe/<airframe_id>', methods=['GET', 'POST'])
def edit_airframe(airframe_id=0):
    if request.method == "POST":
        connection.edit_airframe(request.form, airframe_id)
        return "success"
    return render_template("edit-airframe.html", airframe=airframe_id)

@airframes.route('/delete-airframe/<airframe_id>', methods=['POST'])
def delete_airframe(airframe_id=0):
    if request.method == "POST":
        connection.delete_airframe(airframe_id)
        return redirect(list_airframe())