from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=255,null=True)
	pub_date = models.DateTimeField(null=True)
	image = models.ImageField(upload_to='images/')
	body = models.TextField(null=True)
	link = models.CharField(max_length=255,null=True)
	github = models.CharField(max_length=255,null=True)
	heading = models.CharField(max_length=255,null=True)
	description = models.TextField(null=True)
	plan_of_attack = models.TextField(null=True)
	para1 = models.TextField(null=True)
	para2 = models.TextField(null=True)
	para3 = models.TextField(null=True)
	para4 = models.TextField(null=True)
	model_image = models.ImageField(upload_to='images/',null=True)
	
	def __str__(self):
		return self.title
		
	