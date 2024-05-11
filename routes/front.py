from flask import Blueprint, app, redirect, render_template, request
import connection
from classes.dispatch import Dispatch

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