from django.http import Http404
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from index.serializers import *
from index.models import *
from rest_framework import permissions


class Bron(APIView):
	
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, pk):
		username = request.user.username
		print(username)
		cont = Opisanie.objects.get(pk=pk)
		serializer = HohoSerializer(cont)
		title = serializer.data['name']

		serializer1 = BronSerializer(data=request.data)
		if serializer1.is_valid():
			number = serializer1.data['number']
			date = serializer1.data['date']
			time = serializer1.data['time']
			#name = serializer1.data['name']
			print(title)
			ppp = {
				'hotel': title,
				'number': number,
				'date': date,
				'time': time,
				'name': username
			}

			serializer_save = BronSaveSerializer(data = ppp)
			if serializer_save.is_valid():
				serializer_save.save()
				return Response(serializer_save.data)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
