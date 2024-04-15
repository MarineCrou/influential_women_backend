from marshmallow import fields
from app import march
from models.women_model import WomenProfileModel
from serializers.contributions_serializer import ContributionsSerializer
from serializers.user_serializer import UserSerializer

class WomenSerializer(march.SQLAlchemyAutoSchema):

    contributions = fields.Nested(ContributionsSerializer, many=True) # Telling marshmallow to include contributions inside each profile, when serializing

    class Meta:
        model = WomenProfileModel
        load_instance = True
        include_fk = True
        load_only = ("name",)