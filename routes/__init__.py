from flask import Flask, Blueprint, render_template, request
import connection

routes = Blueprint("routes", __name__, static_folder="static", template_folder="templates")

@routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        icaoCode = request.form['icaoCode']
        return "success"
    return render_template("index.html")