from django.urls import path 
from .views import * 

urlpatterns = [
	path("", MyAccount.as_view()),
]