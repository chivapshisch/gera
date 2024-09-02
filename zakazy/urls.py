from django.urls import path 
from .views import * 

urlpatterns = [ 
	path("bron/<int:pk>/", Bron.as_view()),
	#path("bron/<int:pk>/end/")
]