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

db = SQLAlchemy(app)
march = Marshmallow(app)
bcrypt = Bcrypt(app) # Instantiate bcrypt

# Import users AND teas controllers
from controllers import women_controller, contributions_controller

# Import Blueprints :
app.register_blueprint(women_controller.router_women, url_prefix="/api")
print("BLUEPRINT: Women running 🙋‍♀️🙋‍♀️🙋‍♀️ - APP.PY")

app.register_blueprint(contributions_controller.router_contribution, url_prefix="/api")
print("BLUEPRINT: contributions running 🎉🎉🎉 - APP.PY")