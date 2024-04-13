from marshmallow import fields
from app import march
from models.contribution_model import ContributionModel

class ContributionsSerializer(march.SQLAlchemyAutoSchema):
    class Meta:
        model = ContributionModel
        load_instance = True
        # # ! Now include the user_id when serializing.
        include_fk = True
        # load_only = ("woman_id",)  # Specify fields that should only be used for loading and not returned in serialization
        # dump_only = ("id",)  # Fields that should only be returned in serialization
