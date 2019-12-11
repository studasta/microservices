from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
	role = models.CharField(max_length=15)
	login = models.CharField(max_length=30)
	password = models.CharField(max_length=30)

	def __str__(self):
		return (self.first_name + self.last_name)