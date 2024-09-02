from rest_framework import serializers, fields
from .models import *




class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City 
		fields = ('town')

class OcenkaShowSerializer(serializers.Serializer):
	res = serializers.FloatField()
	golosa = serializers.IntegerField()


class HotelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Opisanie
		fields = ('name','placesbeside','character', 'bbb', 'address', 'house', 'stroenie')


class NameSerializer(serializers.ModelSerializer):
	opisanie = HotelSerializer(read_only=True, many=True)
	class Meta: 
		model = Names 
		fields = ('title', 'opisanie' )

class FindSerializer(serializers.ModelSerializer):
	class Meta:
		model = City 
		fields = ("town",)

class OnlyNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Opisanie
		fields = ("name",)
