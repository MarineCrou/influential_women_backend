
from datetime import datetime, timedelta
import jwt
from sqlalchemy.ext.hybrid import hybrid_property
from app import db, bcrypt
from models.base_model import BaseModel
# from models.women_model import WomenProfileModel
# from models.contribution_model import ContributionModel
from config.environment import SECRET


class UserModel(db.Model, BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=True)
    role = db.Column(
        db.Enum('contributor', 'super_admin', name='roles'),
        default='contributor',
        nullable=False )

    # ! Add opposite relationship here
    women = db.relationship('WomenProfileModel', back_populates='user')
    contributions = db.relationship('ContributionModel', back_populates='user')

    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, password_plaintext):
        encoded_pw = bcrypt.generate_password_hash(password_plaintext)
        self.password_hash = encoded_pw.decode("utf-8")

    def validate_password(self, password_plaintext):
        return bcrypt.check_password_hash(self.password_hash, password_plaintext)

    def generate_token(self):

        payload = {
            "exp": datetime.utcnow() + timedelta(days=7),
            "iat": datetime.utcnow(),
            "sub": self.id,
            "role": self.role
        }

        token = jwt.encode(
            payload,
            SECRET,
            algorithm="HS256"
        )

        return token
