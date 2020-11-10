from rest_framework import viewsets
from olymp.api import serializers
from olymp import models

class OlympViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OlympSerializer
    queryset = models.Olymp.objects.all()