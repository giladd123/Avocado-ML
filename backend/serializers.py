from rest_framework import serializers
from .models import AvocadoInput, AvocadoOutput

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvocadoInput
        fields = "__all__"

class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvocadoOutput
        fields = "__all__"