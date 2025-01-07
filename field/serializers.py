from rest_framework import serializers
from .models import Field

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ["id", "farmer_id", "name", "size_in_hectares", "location", "crop_type"]
