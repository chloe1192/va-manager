from flask import Blueprint, jsonify, render_template, request, flash
from flask_login import login_required, current_user
from . import db
from .models import Note
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    pass
        
@views.route('/aircraft-data')
def aircraft_data():
    return render_template("aircraft-data.html", user=current_user)
    