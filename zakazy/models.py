from django.db import models
from index.models import *

class Sucsesful(models.Model):
	type = models.CharField(max_length = 4)

	def __str__(self):
		return self.type


class Bron(models.Model):
	hotel = models.ForeignKey(Names, on_delete = models.CASCADE, related_name = 'erer', null=True, blank= True)
	number = models.IntegerField()
	date = models.DateField()
	time = models.TimeField(auto_now=False)
	name = models.CharField(max_length = 150)
	sostoinie = models.ForeignKey(Sucsesful, on_delete = models.CASCADE, related_name = 'sostoinie', null=True, blank= True, default = 2)

	def __str__(self):
		return self.name


 