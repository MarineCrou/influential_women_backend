
from http import HTTPStatus
from marshmallow.exceptions import ValidationError

from flask import Blueprint, request
from app import db

# ! import user model
from models.user_model import UserModel
from models.women_model import WomenProfileModel

from serializers.user_serializer import UserSerializer
user_serializer = UserSerializer()

router_user = Blueprint("users", __name__)


@router_user.route('/signup', methods=["POST"])
def signup():
    try:
        user_dictionary = request.json
        print('in signup', user_dictionary)

        user_model = user_serializer.load(user_dictionary)
        user_model.save()
        print("user model", user_model.password)

        return user_serializer.jsonify(user_model)
    except ValidationError as e:
        return { "errors": e.messages, "message": "Something went wrong" }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return { "message": "Something went wrong" }, HTTPStatus.INTERNAL_SERVER_ERROR


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
    
    return { "token": token, "message": "Welcome back!" }


@router_user.route('/user/<int:user_id>', methods=['GET'])
def get_contributions_per_user(user_id):
    user_profile = db.session.query(WomenProfileModel).get(user_id)
    if not user_profile:
        return {"message": "No user profile found"}, HTTPStatus.NOT_FOUND
    print('User found ! - user Controller')
    return user_serializer.jsonify(user_profile)