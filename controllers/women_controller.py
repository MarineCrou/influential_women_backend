# Only the super Admin should have access to the profiles
from http import HTTPStatus
import logging
import random
from marshmallow.exceptions import ValidationError
from flask import Blueprint, request, g
from sqlalchemy.orm import joinedload

# Connecting to the DB
from app import db
from middleware.secure_route_contributor import secure_route_contributor
from middleware.secure_route_admin import secure_route_admin
from models.women_model import WomenProfileModel
from models.contribution_model import ContributionModel

# serializing /deserializing
from serializers.women_serializer import WomenSerializer
from serializers.contributions_serializer import ContributionsSerializer

women_serializer = WomenSerializer() # Instantiate serializer => an instance is a single, unique object // Classes serve as blueprints or templates for creating objects (instances)
contributions_serializer = ContributionsSerializer()

#blueprint for the women's database/table
router_women = Blueprint("women", __name__)


# ! Routes needed for the front end : 
# 1. Get all of the profiles WITH ALL attached contributions
# 2. Get 1 profile, with ALL attached contributions 
# 3. Get 1 profile with latest APPROVED contribution => to display on front-end latest changes for that profile 
# 4. Edit a profile => through Adding a new contribution
# 5. Delete a Profile => When profile is deleted, it will automatically delete all the associated contributions !
# 6. CREATE 1 profile : POST SIMULTANEOUSLY BOTH A NEW WOMAN PROFILE + IT'S CONTRIBUTION <3


# ?---------------------- NO AUTHENTIFICATION NEEDED routes -------------------------------------
# 3. Get 1 profile with latest APPROVED contribution => to display on front-end latest changes for that profile 
@router_women.route("/women/<int:woman_id>", methods=['GET'])
def get_single_woman_with_latest_update(woman_id):
    woman_profile = db.session.query(WomenProfileModel).get(woman_id)
    try : 
        if not woman_profile:
            return {"message": "No woman profile found"}, HTTPStatus.NOT_FOUND
        
        latest_contribution = ContributionModel.query.filter_by(woman_id=woman_id, status="Approved").order_by(ContributionModel.reviewed_at.desc()).first()
        response_data = {
            'woman': women_serializer.dump(woman_profile),
            'latest_contribution': contributions_serializer.dump(latest_contribution)
        }
        return response_data['woman'], HTTPStatus.OK
    except ValidationError as e:
        # db.session.rollback()
        return {"errors": e.messages}, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")  # Log the error
        # db.session.rollback()  # Rollback in case of any other Exception
        print(e)
        return { "message": "No Updates" }, HTTPStatus.UNPROCESSABLE_ENTITY

# 1. Get all profiles WITH their attached contributions
@router_women.route("/women", methods=['GET'])
def get_all_women_profiles():
    logging.debug("Fetching all women profiles")
    try:
        women = WomenProfileModel.query.all()
        if not women:
            logging.debug("No women profiles found")
            return {"message": "No woman profile found"}, HTTPStatus.NOT_FOUND

        result = women_serializer.dump(women, many=True)
        logging.debug(f"Serialized data: {result}")
        return result, HTTPStatus.OK

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return {"message": "Server error"}, HTTPStatus.INTERNAL_SERVER_ERROR

# Get Random Woman featured on home page every week
@router_women.route("/women/featuredProfile", methods=['GET'])
def select_random_profile():
    get_all_profile_ids = db.session.query(WomenProfileModel.id).all()  # Get all profile IDs
    random_id = random.choice(get_all_profile_ids)[0]  # Select a random ID
    profile = WomenProfileModel.query.get(random_id)  # Retrieve the corresponding profile
    return women_serializer.jsonify(profile)

# ?---------------------- Contributor routes -------------------------------------
# 6. POST SIMULTANEOUSLY BOTH A NEW WOMAN PROFILE + IT'S CONTRIBUTION <3
@router_women.route("/women/NewProfile", methods=['POST'])
@secure_route_contributor
def add_profile_with_contributions():
    new_woman_object = request.json
    contributions_data = new_woman_object.pop('contributions', [])  # Extract contributions

    if not contributions_data:
        return {"error": "Contributions data is required"}, 400

    try:
        # Assume first contribution's name is the name for the woman's profile
        new_woman_object['name'] = contributions_data[0]['name']
        new_woman_object['user_id'] = g.current_user.id

        new_woman = women_serializer.load(new_woman_object)
        db.session.add(new_woman)
        db.session.flush()  # Flush to obtain the new woman ID before creating contributions

        for contribution_dict in contributions_data:
            contribution_dict['woman_id'] = new_woman.id  # Link each contribution to the new woman
            contribution_dict['user_id'] = g.current_user.id
            new_contribution = contributions_serializer.load(contribution_dict)
            db.session.add(new_contribution)

        db.session.commit()
        return {"woman": women_serializer.dump(new_woman)}, 201

    except ValidationError as e:
        db.session.rollback()
        return {"errors": e.messages}, 422
    except Exception as e:
        db.session.rollback()
        return {"message": "An error occurred", "details": str(e)}, 500
        

# 4. Edit a profile => through Adding a new contribution
@router_women.route("/women/<int:woman_id>", methods=['POST'])
@secure_route_contributor
def edit_profile_contribution(woman_id):
    print(f"Route accessed for woman ID: {woman_id}")
    json_object = request.json  #get JSON object
    existing_woman = WomenProfileModel.query.get(woman_id) #get Women's profile
    
    if not existing_woman:
        return {"message": "No profile found"}, HTTPStatus.NOT_FOUND
    
    contributions_object = json_object.pop('contributions', []) # To get solely the contributions
    new_contributions = [] # List to hold new contributions for serialization response

    try:
        updated_woman = women_serializer.load(json_object, instance=existing_woman, partial=True) # Update the woman profile without contributions first. Partial=true, means all fields do not have to be completed, for the data to be submitted
        print(updated_woman)
        # Process contributions
        for contribution_dict in contributions_object: #getting the dictionary inside of the contributions nested object
            contribution_dict['woman_id'] = updated_woman.id #not replacing the woman's ID -> ensuring that each contribution is linked to her by setting their woman_id to her id.
            contribution_dict['user_id'] = g.current_user.id
            print(f"this is the woman id {contribution_dict['woman_id']}")
            new_contribution = contributions_serializer.load(contribution_dict)  # Deserialize contribution data
            db.session.add(new_contribution)  # Add to the database session
            new_contributions.append(new_contribution)  # Add to list for response
            print(new_contribution)
        
        db.session.commit()
        # Serialize and return the new contributions
        return {
            'woman': existing_woman,
            'contributions': contributions_serializer.dump(new_contributions, many=True)
        }, HTTPStatus.CREATED

    except ValidationError as e:
        return {"errors": e.messages}, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        return {"message": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
                    


# ?---------------------- ADMIN ONLY routes -------------------------------------

# 2. Get 1 profile, with ALL attached contributions 
@router_women.route("/woman/<int:woman_id>", methods=['GET']) # woman_id in the path and as the argument, must match
@secure_route_admin
def get_single_woman(woman_id ):
    single_profile = db.session.query(WomenProfileModel).get(woman_id)
    print(single_profile)
    if not single_profile:
        return {"message": "No woman's profile found"}, HTTPStatus.NOT_FOUND
    print('Profile found ! - Woman Controller')
    return women_serializer.jsonify(single_profile)


# 5. Delete a Profile => When profile is deleted, it will automatically delete all the associated contributions !
@router_women.route("/women/<int:woman_id>", methods=['DELETE'])
@secure_route_admin
def delete_plant(woman_id):
    profile_to_delete = db.session.query(WomenProfileModel).get(woman_id)

    if not profile_to_delete:
        return {"message": "No profile found"}, HTTPStatus.NOT_FOUND

    db.session.delete(profile_to_delete)
    db.session.commit()

    # return women_serializer.jsonify(profile_to_delete)
    return '', HTTPStatus.NO_CONTENT # handle delete, with an empty body/response


# ?---------------------- Other Routes / TBD IF USEFUL ---------------------------------
#Add a new profile
# @router_women.route("/women", methods=['POST'])
# @secure_route_admin
# def add_1_profile():
#     new_profile = request.json
#     try: 
#         get_request_json = women_serializer.load(new_profile)
#         db.session.add(get_request_json)
#         db.session.commit()

#         return women_serializer.jsonify(get_request_json)

#     except ValidationError as e:
#         return { "errors": e.messages, "message": "Something went wrong, please try again" }, HTTPStatus.UNPROCESSABLE_ENTITY
#     except Exception as e:
#         print(e)
#         return { "message": f"{new_profile["name"]} already exisists" }, HTTPStatus.UNPROCESSABLE_ENTITY
    