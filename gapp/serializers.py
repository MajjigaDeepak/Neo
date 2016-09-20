from gapp.models import Query
from rest_framework import serializers


class querySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
