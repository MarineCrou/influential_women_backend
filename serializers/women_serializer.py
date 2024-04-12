from marshmallow import fields
from app import march
from models.women_model import WomenProfileModel
from models.contribution_model import ContributionModel

class WomenSerializer(march.SQLAlchemyAutoSchema):

    # contributions = fields.Nested('CommentSchema', many=True)
    # user = fields.Nested(UserSerializer, many=False) # # Telling marshmallow to include a User inside our tea, when serializing

    class Meta:
        model = WomenProfileModel
        load_instance = True
        # # ! Now include the user_id when serializing.
        # include_fk = True
    