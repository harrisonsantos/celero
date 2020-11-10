from rest_framework import serializers
from olymp import models

class OlympSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Olymp
        fields = '__all__'