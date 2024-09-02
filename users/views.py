from django.http import Http404
from .models import *
#from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from zakazy.models import *
from zakazy.serializers import *
import json
from .serializers import *

class MyAccount(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request):
		username = 	request.user.username

		stil = [
		{
			"username": username,
		}
		]
		print(stil)
		serializer_name = AccountSerializer(stil, many = True)
		mnogo = [
		{
			"hotel": i.hotel,
 			"number": i.number,
			"date": i.date,
			"time": i.time,

		} for i in Bron.objects.filter(name = username)
		]

		serializer = BronAccountSerializer(mnogo, many =True)
		
		return Response(serializer_name.data + serializer.data)
