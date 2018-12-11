from django.db import models

# Create your models here.

class CatsDogs(models.Model):
	name = models.CharField(max_length=255,null=True)
	img = models.ImageField(upload_to='files/')
	
	def __str__(self):
		return self.name
