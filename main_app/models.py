from django.db import models

# Create your models here.

class User(models.Model):
	# u_id = models.BigAutoField(primary_key = True)
	first_name = models.CharField(max_length = 64)
	last_name = models.CharField(max_length = 64)
	password = models.CharField(max_length = 64,blank= True)

class image(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE);
	result = models.BooleanField(null = True)
