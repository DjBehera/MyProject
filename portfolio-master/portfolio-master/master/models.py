

from django.db import models

# Create your models here.

class Master(models.Model):
	name = models.CharField(max_length=255,null=True)
	cid = models.CharField(max_length=255,null=True)
	csv = models.FileField(upload_to='files/')
	
	def __str__(self):
		return self.cid
