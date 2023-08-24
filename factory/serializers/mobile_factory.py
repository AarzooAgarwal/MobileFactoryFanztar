from factory.constants import CONSTANTS
from rest_framework import serializers

class CreateOrderSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        if data.get("components") is None:
            error = CONSTANTS.MISSING.COMPONENTS
            raise serializers.ValidationError({"status": error[0], "message": error[1]})