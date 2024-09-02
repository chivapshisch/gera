from django.db import models



 
class Names(models.Model):
	title = models.CharField(max_length = 150)


	def __str__(self):
		return self.title

class City(models.Model):
	town = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.town


class Opisanie(models.Model):
	name = models.ForeignKey(Names, on_delete = models.CASCADE, related_name = 'opisanie', null=True, blank= True)
	placesbeside = models.CharField(max_length = 200)
	character = models.CharField(max_length = 200)
	bbb = models.ForeignKey(City, on_delete = models.CASCADE, related_name = 'gorod', null=True, blank= True)
	address = models.CharField(max_length = 300)
	house = models.IntegerField()
	stroenie = models.IntegerField(blank = True, null = True)

	def __unicode__(self):
		return self.name


