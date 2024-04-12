from app import db
from models.base_model import BaseModel
from models.women_model import WomenProfileModel

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
     
     name = db.Column(db.Text, nullable=False, unique=True)
     date_of_birth = db.Column(db.String, nullable=True)
     nationality= db.Column(db.String, nullable=False)
     img = db.Column(db.String(255), nullable=True)
     bio = db.Column(db.Text, nullable=True)
     achievements = db.Column(db.Text, nullable=True)
     additionnal_content = db.Column(db.Text, nullable=True)
     status = db.Column(db.Enum('Pending Review', 'Approved', 'Rejected', name='status_types'), default='Pending Review', nullable=False ) # "Pending Review", "Accepted", "Rejected"
     # created + reviewed times => imported from the basemodel
     
     # ! Foreign Keys
     woman_id = db.Column(db.Integer, db.ForeignKey('women.id'), nullable=True) # referencing the table name and column name of the foreign key target (__tablename__='women')
     # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
     # ! Connecting to the DB
     woman = db.relationship('WomenProfileModel', backref="women") # ? Connecting the plant model to the user model (check notion for `backref`)
     # user = db.relationship('UserModel', backref="plants") # ? Connecting the plant model to the user model (check notion for `backref`)
     
     