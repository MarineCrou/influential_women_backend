# both the contributers(users) and the Admin will have the ability Edit Add to the Data
# only the Admin will be allowed to Delete info !

from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from flask import Blueprint, request, g

# Connecting to the DB
from app import db
from models.contribution_model import ContributionModel

# serializing /deserializing
from serializers.contributions_serializer import ContributionsSerializer
contribution_serializer = ContributionsSerializer() # Instantiate serializer => an instance is a single, unique object // Classes serve as blueprints or templates for creating objects (instances)

#blueprint for the women's database/table
router_contribution = Blueprint("contributions", __name__)

# ! Contributor routes
# ? get all the contributions 
@router_contribution.route("/contributions", methods=['GET']) 
def get_all_contributions():
    contributions = ContributionModel.query.all()
    return contribution_serializer.jsonify(contributions, many=True)


# ? Add a New Contribution
@router_contribution.route("/contributions", methods=['POST'])
def add_new_contribution():
    new_contribution = request.json
    try:
        get_request_json = contribution_serializer.load(new_contribution)
        db.session.add(get_request_json)
        db.session.commit()

        return contribution_serializer.jsonify(get_request_json)

    except ValidationError as e:
        return { "errors": e.messages, "message": "Something went wrong, please try again" }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return { "message": "Something went wrong" }, HTTPStatus.INTERNAL_SERVER_ERROR

# ? Edit a contribution
@router_contribution.route("/contributions/<int:contribution_id>", methods=['PUT'])
def edit_profile(contribution_id):
    try:
        profile_exists = db.session.query(ContributionModel).get(contribution_id) #getting existing tea
        if not profile_exists:
            return {"message": "No plant found"}, HTTPStatus.NOT_FOUND
    
        get_json = request.json
        edited_profile = contribution_serializer.load(get_json, instance=profile_exists, partial=True) #marshmallow serializer
        
        # plant_model_data.user_id = g.current_user.id # ! Instead of hardcoding, here is the current user id
        db.session.commit() #save the edited profile

        return contribution_serializer.jsonify(edited_profile)
    except ValidationError as e: #issue lies with the client's input
        return { "errors": e.messages, "message": "Something went wrong, please try again" }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return { "message": "Something went wrong" }, HTTPStatus.INTERNAL_SERVER_ERROR

# ! Admin Only Routes  

# ? Get all contributions for 1 profile card
@router_contribution.route("/contributions/woman/<int:woman_id>", methods=['GET']) 
def get_profile_contributions(woman_id):
   # Fetch contributions by woman_id
    contributions = ContributionModel.query.filter_by(woman_id=woman_id).all()

    if not contributions:
        return {"message": "No contributions found for this profile 😖"}, HTTPStatus.NOT_FOUND

    return contribution_serializer.jsonify(contributions, many=True)


# ? Get All contributions based on status => only for Admin
@router_contribution.route("/contributions/status/<string:status>", methods=['GET'])
def get_by_status(status):
    valid_statuses = ['Approved', 'Rejected', 'Pending Review']
    if status not in valid_statuses:
        return {"message": "Invalid status provided"}, HTTPStatus.BAD_REQUEST

    contributions = ContributionModel.query.filter_by(status=status).all()

    if not contributions:
        return {"message": "No contributions found for that status"}, HTTPStatus.NOT_FOUND

    # Assuming contribution_serializer is set up to handle lists
    return contribution_serializer.jsonify(contributions, many=True)
    
# ? Get contributions per woman_id + Status


# ? Delete A contribution => only for Admin
@router_contribution.route("/contributions/<int:contribution_id>", methods=['DELETE'])
def delete_plant(contribution_id):
    profile_to_delete = db.session.query(ContributionModel).get(contribution_id)

    if not profile_to_delete:
        return {"message": "No profile found"}, HTTPStatus.NOT_FOUND

    db.session.delete(profile_to_delete)
    db.session.commit()

    # return women_serializer.jsonify(profile_to_delete)
    return '', HTTPStatus.NO_CONTENT # handle delete, with an empty body/response