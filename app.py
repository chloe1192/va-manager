from flask import Flask, render_template, request
from routes.airframes import airframes
from routes.admin import admin
from routes.front import front

app = Flask(__name__)
app.register_blueprint(airframes, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(front, url_prefix='/')

if __name__ == "__main__":
    app.run(debug=True)