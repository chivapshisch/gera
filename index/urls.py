from django.urls import path, re_path
from .views import *

urlpatterns = [

	path("hotel/", HotelList.as_view()),
	path("find/", FindList.as_view()),
	path("read/<int:pk>/", DetailList.as_view()),

	
	]