
from http import HTTPStatus
import pprint
from marshmallow.exceptions import ValidationError

from flask import Blueprint, g, request
from app import db
from middleware.secure_route_admin import secure_route_admin
from middleware.secure_route_contributor import secure_route_contributor
from models.contribution_model import ContributionModel

# ! import user model
from models.user_model import UserModel
from models.women_model import WomenProfileModel

from serializers.user_serializer import UserSerializer
from serializers.contributions_serializer import ContributionsSerializer
user_serializer = UserSerializer()
contribution_serializer = ContributionsSerializer()

router_user = Blueprint("users", __name__)


@router_user.route('/signup', methods=["POST"])
def signup():
    user_dictionary = request.json

    # ! Check the passwords
    if user_dictionary['password'] != user_dictionary['passwordConfirmation']:
        return {"errors": "Passwords do not match", "messsages": "Something went wrong"}, HTTPStatus.UNPROCESSABLE_ENTITY
    
    # ! Delete the password conf field that marshmallow doesn't know about.
    del user_dictionary['passwordConfirmation']
# Adding additional error hangling -> sending back the right object when someone that already exists tries to log in 
    try:
        user = user_serializer.load(user_dictionary)
        user.save()
    except ValidationError as e:
        return { "errors": e.messages, "message": "Something went wrong" }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return { "message": "Something went wrong" }, HTTPStatus.INTERNAL_SERVER_ERROR

    return user_serializer.jsonify(user)

@router_user.route('/login', methods=["POST"])
def login():
    # ! user provides a email & password
    user_dictionary = request.json
    
    # Check if the user with this email exists
    user = UserModel.query.filter_by(email=user_dictionary["email"]).first()
    
    # If there's no user found:
    if not user:
        return { "message": "Your email or password was incorrect." }, HTTPStatus.UNAUTHORIZED
    
    # Validate the password against database password
    if not user.validate_password(user_dictionary["password"]):
        return { "message": "Your email or password was incorrect." }, HTTPStatus.UNAUTHORIZED
    
    # Make a token and send it back!
    token = user.generate_token()
    
    return { "token": token, "message": f"Welcome back {user.username}!" }


# ? ------------------- PERMISSIONS ----------------------------------
# ! Get a single user with all of their contributions 
# Should it be accessable to the current user, to see all of their contributions ? As a history ?
@router_user.route('/user/<int:user_id>', methods=['GET'])
# @secure_route_admin
def get_contributions_per_user(user_id):
    user_profile = db.session.query(UserModel).get(user_id)
    if not user_profile: 
        return {"message": "No user found"}, HTTPStatus.NOT_FOUND
    return user_serializer.jsonify(user_profile)

#get logged in user
@router_user.route('/user')
@secure_route_contributor
def get_my_data():
    # g.current_user is already set by the decorator secure_route_contributor
    data = {"id": g.current_user.id, "username": g.current_user.username, "email": g.current_user.email, "role":g.current_user.role}
    return data, HTTPStatus.OK