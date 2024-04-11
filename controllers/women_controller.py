from flask import Blueprint
from app import db
from models.women_model import WomenProfileModel

#blueprint for the women's database/table
router_women = Blueprint("women", __name__)


@router_women.route("/inlfuential_women", methods=['GET']) #get all the influential women
def get_all_women():
    get_women = db.sessions.query(WomenProfileModel).all()
    return #serializer
