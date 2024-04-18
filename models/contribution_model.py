from app import db
from models.base_model import BaseModel

class ContributionModel(db.Model, BaseModel):
     __tablename__='contribution'
     
     id = db.Column(db.Integer, primary_key=True)
     contribution_type = db.Column(db.Enum(
        'New Profile Creation',
        'Image Upload/Edit',
        'Bio Edit',
        'Achievements Edit',
        'Additional Content Edit',
        'Correction Submission',
        'Historical Context Addition',
        'Other',
        name='contribution_types'),
        nullable=False, 
        default="Achievements Edit"
    )
     
     name = db.Column(db.Text, nullable=False)
     date_of_birth = db.Column(db.String, nullable=True)
     nationality= db.Column(db.String, nullable=False)
     img = db.Column(db.String, nullable=True)
     bio = db.Column(db.Text, nullable=True)
     achievements = db.Column(db.Text, nullable=True)
     additionnal_content = db.Column(db.Text, nullable=True)
     field = db.Column(db.Text, nullable=True)
     status = db.Column(
          db.Enum('Pending Review', 'Approved', 'Rejected', name='status_types'),
          default='Pending Review',
          nullable=False ) # "Pending Review", "Accepted", "Rejected"
     # created + reviewed times => imported from the basemodel
     
     # ! connecting to the Women Model
     woman_id = db.Column(db.Integer, db.ForeignKey('women.id'), nullable=False)
     woman = db.relationship('WomenProfileModel', back_populates='contributions')
     
     # ! Connecting to the User
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True) # create user_id column in contribudtion model
     user = db.relationship('UserModel', back_populates='user_contributions') # create the relationship to the user's model