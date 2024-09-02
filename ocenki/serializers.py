from rest_framework import serializers 
from .models import * 
from index.models import *


class OcenOtkr(serializers.ModelSerializer):
	class Meta:
		model = Mnenie
		fields = ("name",)

class OcenkaSerializer(serializers.Serializer):
	name = serializers.CharField()
	ball = serializers.IntegerField()
	author = serializers.CharField()


class ModelOc(serializers.ModelSerializer):
	class Meta:
		model = Mnenie 
		fields = ('name', 'ball', 'author')

class ErrorSerializer(serializers.Serializer):
	error = serializers.CharField()