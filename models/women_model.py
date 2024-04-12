from app import db
from models.base_model import BaseModel

class WomenProfileModel(db.Model, BaseModel):
    __tablename__='women'

    id = db.Column(db.Integer, primary_key=True) # primary key
    is_featured_month = db.Column(db.Boolean, nullable=False)

    # ! getting the USER ID
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) #? Creating UserId Column in the DB
    # user = db.relationship('UserModel', backref="plants") # ? Connecting the women model to the user model (check notion for `backref`/ use back_populate)