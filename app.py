from flask import Flask, render_template, request
from routes import routes
from routes.airframes import airframes
from routes.admin import admin

app = Flask(__name__)
app.register_blueprint(routes, url_prefix='/')
app.register_blueprint(airframes, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')

if __name__ == "__main__":
    app.run(debug=True)