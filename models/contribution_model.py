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
     
     name = db.Column(db.Text, nullable=False, unique=False)
     date_of_birth = db.Column(db.String, nullable=True)
     nationality= db.Column(db.String, nullable=False)
     img = db.Column(db.String(255), nullable=True)
     bio = db.Column(db.Text, nullable=True)
     achievements = db.Column(db.Text, nullable=True)
     additionnal_content = db.Column(db.Text, nullable=True)
     status = db.Column(
          db.Enum('Pending Review', 'Approved', 'Rejected', name='status_types'),
          default='Pending Review',
          nullable=False ) # "Pending Review", "Accepted", "Rejected"
     # created + reviewed times => imported from the basemodel
     
     # ! connecting to the Women Model
     woman_id = db.Column(db.Integer, db.ForeignKey('women.id'), nullable=True)
     woman = db.relationship('WomenProfileModel', back_populates='contributions')
     
     # ! Connecting to the user mode
     # user = db.relationship('UserModel', backref="plants") # ? Connecting the contributions model to the user model (check notion for `backref`)
     # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
     
     