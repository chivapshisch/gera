from django.http import Http404
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ocenki.serializers import *
from ocenki.models import * 



class HotelList(generics.ListAPIView):
	queryset = Names.objects.all()
	serializer_class = NameSerializer
	permission_classes = [permissions.IsAuthenticated]
	def my_view(request):
			username = None
			if request.user.is_authenticated():
				username = request.user.username
				print(username)

 
class FindList(APIView):
	def post(self, request):
		serializer1 = FindSerializer(data=request.data)
		if serializer1.is_valid():
			zapr = serializer1.data['town']
			
			
			snip = Opisanie.objects.filter(bbb = zapr)
			for i in snip:
				serializer2 = OnlyNameSerializer(snip, many = True)
				return Response(serializer2.data)

			
class DetailList(APIView):
	def get(request, self, pk):
		try:
			cont = Opisanie.objects.get(pk=pk)
			
			serializer = HotelSerializer(cont)

			
			name_for_poisk = serializer.data['name']



			cont_ocenka = Mnenie.objects.filter(name = name_for_poisk)

			ilist = []
			for i in cont_ocenka:
				ilist.append(int(i.ball))

			golosa = len(ilist)
			end = sum(ilist)/golosa
			res = round(end, 1)
		
			print(type(golosa))
			mnogo = [ 
			{
				"res": res, 
				"golosa": golosa
			}
			]
			serializer_2 = OcenkaShowSerializer(data = mnogo, many = True)
			print('ok')
			
			if serializer_2.is_valid():
				print('ok')
				return Response(serializer_2.data + serializer.data)

			#else: 
			#	errr = 'No'
			#	return Response(errr)
		

		except Names.DoesNotExist:
			raise Http404







