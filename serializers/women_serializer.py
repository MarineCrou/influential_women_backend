import logging
from marshmallow import fields, post_dump
from app import march
from models.contribution_model import ContributionModel
from models.women_model import WomenProfileModel
from serializers.contributions_serializer import ContributionsSerializer
from serializers.user_serializer import UserSerializer

class WomenSerializer(march.SQLAlchemyAutoSchema):

    contributions = fields.Nested(ContributionsSerializer, many=True) # Telling marshmallow to include contributions inside each profile, when serializing
    # latest_approved_contribution = fields.Method('get_latest_approved_contribution')

    class Meta:
        model = WomenProfileModel
        load_instance = True
        include_fk = True
        load_only = ("name",)
        
    # def get_latest_approved_contribution(self, obj):
    #     # Ensure the status check is exactly correct, including case sensitivity
    #     approved_contributions = [c for c in obj.contributions if c.status == 'Approved' and c.reviewed_at is not None]

    #     if approved_contributions:
    #         # Find the contribution with the latest review date
    #         latest_approved = max(approved_contributions, key=lambda x: x.reviewed_at)
    #         return ContributionsSerializer().dump(latest_approved)
    #     logging.debug(f"Total contributions for {obj.name}: {len(obj.contributions)}")
    #     logging.debug(f"Approved contributions: {approved_contributions}")
    #     return None