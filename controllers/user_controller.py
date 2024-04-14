
from http import HTTPStatus

from flask import Blueprint, request
from app import db
from marshmallow.exceptions import ValidationError
from models.contribution_model import ContributionModel

# ! import user model
from models.user_model import UserModel
from models.women_model import WomenProfileModel

from serializers.women_serializer import WomenProfileModel
from serializers.user_serializer import UserSerializer

user_serializer = UserSerializer()

router_user = Blueprint("users", __name__)

@router_user.route('/signup', methods=["POST"])
def signup():
    user_dictionary = request.json
    
    try:
        user = user_serializer.load(user_dictionary)
        user.save()
    except ValidationError as e:
        return {"errors": e.messages, "messsages": "Something went wrong"}

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
    
    return { "token": token, "message": "Welcome back!" }


@router_user.route('/user/<int:woman_id>/contributions', methods=['GET'])
def get_contributions_per_user(woman_id):
    try : 
        # get user 
        user_exists = db.session.query(UserModel).get(woman_id)
        if not user_exists:
            return {"message": "No User Found"}, HTTPStatus.NOT_FOUND
        
        get_user_contributions = ContributionModel.query.filter_by(woman_id=woman_id, status="Approved").order_by(ContributionModel.reviewed_at.desc()).first()
        response_data = {
            'woman': women_serializer.dump(woman_profile),
            'latest_contribution': contributions_serializer.dump(latest_contribution)
        }
        return response_data['latest_contribution'], HTTPStatus.OK
    except ValidationError as e:
        # db.session.rollback()
        return {"errors": e.messages}, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")  # Log the error
        # db.session.rollback()  # Rollback in case of any other Exception
        print(e)
        return { "message": "No Updates" }, HTTPStatus.UNPROCESSABLE_ENTITY