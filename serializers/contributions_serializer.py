from marshmallow import fields
from app import march
from models.contribution_model import ContributionModel
from serializers.user_serializer import UserSerializer

class ContributionsSerializer(march.SQLAlchemyAutoSchema):

    user = fields.Nested(UserSerializer, many=False)
    
    class Meta:
        model = ContributionModel
        load_instance = True
        include_fk = True # includes all connecrted foreign keys, when serializing.

        # load_only = ("woman_id",)  # Specify fields that should only be used for loading and not returned in serialization
        # dump_only = ("id",)  # Fields that should only be returned in serialization
