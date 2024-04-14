from app import db
from models.base_model import BaseModel
# from models.contribution_model import ContributionModel
# from models.user_model import UserModel

class WomenProfileModel(db.Model, BaseModel):
    __tablename__='women'

    id = db.Column(db.Integer, primary_key=True) # primary key
    name = db.Column(db.Text, nullable=False, unique=True)
    is_featured_month = db.Column(db.Boolean, nullable=False)

    # getting the USER ID
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) #? Creating UserId Column in the DB
    user = db.relationship('UserModel', back_populates='women') # ? Using back_populates, the variable name, must match the back_populates name, in the matching model

    #connecting contributions to women's table
    contributions = db.relationship('ContributionModel', back_populates='woman')