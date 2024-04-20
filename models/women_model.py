from app import db
from models.base_model import BaseModel
from models.user_model import UserModel

class WomenProfileModel(db.Model, BaseModel):
    __tablename__='women'

    id = db.Column(db.Integer, primary_key=True) # primary key
    name = db.Column(db.Text, default=False, nullable=True, unique=True)
    is_featured_month = db.Column(db.Boolean, default=False, nullable=True)

    # # getting the USER ID
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) #? Creating UserId Column in the DB
    users = db.relationship('UserModel', back_populates='women') # ? Using back_populates, the variable name, must match the back_populates name from the other model

    # ! connecting contributions to women's table
    contributions = db.relationship('ContributionModel', back_populates='woman', cascade='all, delete-orphan')
    
    # ! This method should loop through all related contributions and update their names to match the profile's name, then save these changes to the database.
    def sync_contributions(self):
        for contribution in self.contributions:
            contribution.name = self.name
        db.session.commit()  # Commit the changes to the database