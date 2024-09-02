from rest_framework import serializers 
from .models import Bron 
from index.models import *

class BronSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bron 
		fields = ('number', 'date', 'time',)

class BronSaveSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bron 
		fields = ('hotel', 'number', 'date', 'time', 'name')

class HohoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Opisanie 
		fields = ('name',)


class BronAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bron 
		fields = ('hotel', 'number', 'date', 'time')


class BronSostoinueSerialzer(serializers.ModelSerializer):
	class Meta: 
		model = Bron 
		fields = ('hotel', 'name', 'sostoinie')