from django.urls import path 
from .views import * 

urlpatterns = [ 
	path("ocen/<int:pk>/", OcenCreate.as_view()),
]