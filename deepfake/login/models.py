from django.db import models

# Create your models here.from django.db import models

class login1(models.Model):
	username = models.CharField(max_length=255,blank=True,null=True)
	password = models.CharField(max_length=255,blank=True,null=True)