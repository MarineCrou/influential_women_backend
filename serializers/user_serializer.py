from marshmallow import fields
from app import march
from models.user_model import UserModel
from serializers.contributions_serializer import ContributionsSerializer

class UserSerializer(march.SQLAlchemyAutoSchema):
    contributions = fields.Nested(ContributionsSerializer, many=True) # Nest all of the contributions of a user
    password = fields.String(required=True)  # Adding a password field
    
    class Meta:
        model = UserModel
        load_instance = True #Deserialize into a model. When you do user_serializer.load, it should return a model.
        load_only = ("password", "password_hash", "email")  #These fields are only allowed when loading
        include_fk = True


# * marshmallow loading => deserialize
# * marshmallow jsonify => serialize