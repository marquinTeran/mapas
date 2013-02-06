from django.db import models
from django.contrib.auth.models import User

class Ubicacion(models.Model):
	nombre = models.CharField(max_length=200)
	lat = models.CharField(max_length=50)
	lng = models.CharField(max_length=50)
	fecha = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre