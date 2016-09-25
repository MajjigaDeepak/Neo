from gapp.models import Query, question
from rest_framework import serializers


class querySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query


class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = question
