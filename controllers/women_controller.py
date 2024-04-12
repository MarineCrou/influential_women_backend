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


@router_women.route("/women/<int:woman_id>", methods=['GET']) # plants_id in the path and as the argument, must 
def get_single_woman(woman_id ):
    single_profle = db.session.query(WomenProfileModel).get(woman_id)
    if not single_profle:
        return {"message": "No woman's profile found"}, HTTPStatus.NOT_FOUND
    print('Profile found ! - Woman Controller')
    return women_serializer.jsonify(single_profle)