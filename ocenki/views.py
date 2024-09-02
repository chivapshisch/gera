from django.http import Http404
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from zakazy.serializers import *
from zakazy.models import *
from index.models import *
from index.serializers import *


class OcenCreate(APIView):
	permission_classes = [permissions.IsAuthenticated]
	def post(self, request, pk):
		try:
			cont = Opisanie.objects.get(pk=pk)
			serializer = HohoSerializer(cont)
					
			name = serializer.data['name']
			author = request.user.username
			ball = request.data['ball']

			try:
				cont_2 = Bron.objects.get(hotel = name, name = author)
				serializer_bron = BronSostoinueSerialzer(cont_2)
				sost = serializer_bron.data['sostoinie']
				print(sost)
				if sost == 1:
					mnogo = [ 
					{
						"name": name,
						"ball": ball,
						"author": author
					}
					]
				
					try: 
						
						opyt = Mnenie.objects.get(name = name, author = author)
						error = 'Один пользователь может оставить только одну оценку'
						return Response(error)
						
					except Mnenie.DoesNotExist: 
						serializer_mnogo = ModelOc(data = mnogo, many = True)
						if serializer_mnogo.is_valid():
							serializer_mnogo.save()
							return Response(serializer_mnogo.data)

				elif sost == 2:
					error = 'Оценку может ставить только человек посетивший отель'
					err_mn = [
					{
						'error': error
					}
					]
					pampam = ErrorSerializer(data = err_mn, many = True)
					if pampam.is_valid():
						return Response(pampam.data)
			
			except Bron.DoesNotExist:
				raise Http404

		except Opisanie.DoesNotExist:
			raise Http404

		


