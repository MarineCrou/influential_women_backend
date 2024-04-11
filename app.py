from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

from config.environment import db_URI 

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello, World!"

app.config['SQLALCHEMY_DATABASE_URI'] = db_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
march = Marshmallow(app)
bcrypt = Bcrypt(app) # Instantiate bcrypt

# Import users AND teas controllers
from controllers import women_controller

# Import Blueprints :
# app.register_blueprint(women_controller.router_women, url_prefix="/api")