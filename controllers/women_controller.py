# Only the super Admin should have access to the profiles


from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from flask import Blueprint, request, g

# Connecting to the DB
from app import db
from models.women_model import WomenProfileModel

# serializing /deserializing
from serializers.women_serializer import WomenSerializer
women_serializer = WomenSerializer() # Instantiate serializer => an instance is a single, unique object // Classes serve as blueprints or templates for creating objects (instances)

#blueprint for the women's database/table
router_women = Blueprint("women", __name__)


@router_women.route("/women", methods=['GET']) #get all the influential women
def get_all_women_profiles():
    women = WomenProfileModel.query.all()
    return women_serializer.jsonify(women, many=True)


@router_women.route("/women/<int:woman_id>", methods=['GET']) # woman_id in the path and as the argument, must 
def get_single_woman(woman_id ):
    single_profile = db.session.query(WomenProfileModel).get(woman_id)
    if not single_profile:
        return {"message": "No woman's profile found"}, HTTPStatus.NOT_FOUND
    print('Profile found ! - Woman Controller')
    return women_serializer.jsonify(single_profile)

@router_women.route("/women", methods=['POST'])
def add_1_profile():
    new_profile = request.json
    try:
        get_request_json = women_serializer.load(new_profile)
        db.session.add(get_request_json)
        db.session.commit()

        return women_serializer.jsonify(get_request_json)

    except ValidationError as e:
        return { "errors": e.messages, "message": "Something went wrong, please try again" }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return { "message": "Something went wrong" }, HTTPStatus.INTERNAL_SERVER_ERROR
    

#edit a profile
@router_women.route("/women/<int:woman_id>", methods=['PUT'])
def edit_profile(woman_id):
    try:
        profile_exists = db.session.query(WomenProfileModel).get(woman_id) #getting existing tea
        if not profile_exists:
            return {"message": "No plant found"}, HTTPStatus.NOT_FOUND
    
        get_json = request.json
        edited_profile = women_serializer.load(get_json, instance=profile_exists, partial=True) #marshmallow serializer
        
        # plant_model_data.user_id = g.current_user.id # ! Instead of hardcoding, here is the current user id
        db.session.commit() #save the edited profile

        return women_serializer.jsonify(edited_profile)
    except ValidationError as e: #issue lies with the client's input
        return { "errors": e.messages, "message": "Something went wrong, please try again" }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return { "message": "Something went wrong" }, HTTPStatus.INTERNAL_SERVER_ERROR


# Delete 1 Profile => When delete the profile, will automatically delete all contributions associated to it !
@router_women.route("/women/<int:woman_id>", methods=['DELETE'])
def delete_plant(woman_id):
    profile_to_delete = db.session.query(WomenProfileModel).get(woman_id)

    if not profile_to_delete:
        return {"message": "No profile found"}, HTTPStatus.NOT_FOUND

    db.session.delete(profile_to_delete)
    db.session.commit()

    # return women_serializer.jsonify(profile_to_delete)
    return '', HTTPStatus.NO_CONTENT # handle delete, with an empty body/response