from django.db import models
from index.models import *


class Mnenie(models.Model):
	name = models.ForeignKey(Names, on_delete = models.CASCADE, related_name = 'nnn', null=True, blank= True)
	ball = models.IntegerField()
	author = models.CharField(max_length = 300)


	def __str__(self):
		return self.author
