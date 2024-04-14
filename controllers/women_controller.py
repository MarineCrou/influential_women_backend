# Only the super Admin should have access to the profiles


from http import HTTPStatus
import logging
from marshmallow.exceptions import ValidationError
from flask import Blueprint, request, g

# Connecting to the DB
from app import db
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
# 4. Edit a profile => In the contribtion controller
# 5. Delete a Profile => When profile is deleted, it will automatically delete all the associated contributions !
# 6. CREATE 1 profile : POST SIMULTANEOUSLY BOTH A NEW WOMAN PROFILE + IT'S CONTRIBUTION <3

# 1. Get all of the profiles WITH ALL attached contributions
@router_women.route("/women", methods=['GET'])
def get_all_women_profiles():
    women = WomenProfileModel.query.all()
    return women_serializer.jsonify(women, many=True)


# 2. Get 1 profile, with ALL attached contributions 
@router_women.route("/women/<int:woman_id>", methods=['GET']) # woman_id in the path and as the argument, must 
def get_single_woman(woman_id ):
    single_profile = db.session.query(WomenProfileModel).get(woman_id)
    if not single_profile:
        return {"message": "No woman's profile found"}, HTTPStatus.NOT_FOUND
    print('Profile found ! - Woman Controller')
    return women_serializer.jsonify(single_profile)



# 3. Get 1 profile with latest APPROVED contribution => to display on front-end latest changes for that profile 
@router_women.route("/women/NewContribution/<int:woman_id>", methods=['GET'])
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
        return response_data['latest_contribution'], HTTPStatus.OK
    except ValidationError as e:
        # db.session.rollback()
        return {"errors": e.messages}, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")  # Log the error
        # db.session.rollback()  # Rollback in case of any other Exception
        print(e)
        return { "message": "No Updates" }, HTTPStatus.UNPROCESSABLE_ENTITY


# 5. Delete a Profile => When profile is deleted, it will automatically delete all the associated contributions !
@router_women.route("/women/<int:woman_id>", methods=['DELETE'])
def delete_plant(woman_id):
    profile_to_delete = db.session.query(WomenProfileModel).get(woman_id)

    if not profile_to_delete:
        return {"message": "No profile found"}, HTTPStatus.NOT_FOUND

    db.session.delete(profile_to_delete)
    db.session.commit()

    # return women_serializer.jsonify(profile_to_delete)
    return '', HTTPStatus.NO_CONTENT # handle delete, with an empty body/response


# 6. POST SIMULTANEOUSLY BOTH A NEW WOMAN PROFILE + IT'S CONTRIBUTION <3
@router_women.route("/women/NewProfile", methods=['POST'])
def add_profile_with_contributions():
    new_woman_data = request.json
    contributions_data = new_woman_data.pop('contributions', []) #To get the contributions key into the contributions_data variable, adn store the list

    try:
        new_woman = women_serializer.load(new_woman_data)
        db.session.add(new_woman)
        db.session.flush()  # Flush to obtain the new woman ID

        for contribution_dict in contributions_data:
            contribution_dict['woman_id'] = new_woman.id
            new_contribution = contributions_serializer.load(contribution_dict)
            db.session.add(new_contribution)

        db.session.commit()
        print ("Success 🎉 - the data has been seeded")

        return {
            'woman': women_serializer.dump(new_woman)
        }, HTTPStatus.CREATED

    except ValidationError as e:
        # db.session.rollback()
        return {"errors": e.messages}, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")  # Log the error
        # db.session.rollback()  # Rollback in case of any other Exception
        print(e)
        return {"message": f"{new_woman_data["name"]} already exisists"}, HTTPStatus.UNPROCESSABLE_ENTITY
        

# ! Other routes : 
    # Add a new profile
# @router_women.route("/women", methods=['POST'])
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
    

# Edit a profile
# @router_women.route("/women/<int:woman_id>", methods=['PUT'])
# def edit_profile(woman_id):
#     try:
#         profile_exists = db.session.query(WomenProfileModel).get(woman_id) #getting existing tea
#         if not profile_exists:
#             return {"message": "No plant found"}, HTTPStatus.NOT_FOUND
    
#         get_json = request.json
#         edited_profile = women_serializer.load(get_json, instance=profile_exists, partial=True) #marshmallow serializer
        
#         # plant_model_data.user_id = g.current_user.id # ! Instead of hardcoding, here is the current user id
#         db.session.commit() #save the edited profile

#         return women_serializer.jsonify(edited_profile)
#     except ValidationError as e: #issue lies with the client's input
#         return { "errors": e.messages, "message": "Something went wrong, please try again" }, HTTPStatus.UNPROCESSABLE_ENTITY
#     except Exception as e:
#         print(e)
#         return { "message": "Something went wrong" }, HTTPStatus.INTERNAL_SERVER_ERROR