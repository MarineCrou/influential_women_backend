from marshmallow import fields
from app import march
from models.user_model import UserModel
from serializers.contributions_serializer import ContributionsSerializer


class UserSerializer(march.SQLAlchemyAutoSchema):
    password = fields.String(required=True)  # Adding a password field
    contributions = fields.Nested(ContributionsSerializer, many=True, attribute='user_contributions') # Nest all of the contributions of a user
    
    class Meta:
        model = UserModel
        load_instance = True #Deserialize into a model. When you do user_serializer.load, it should return a model.
        load_only = ("password", "password_hash", "email")  #These fields are only allowed when loading
        include_fk = True
