from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# add ping count to User

class Ping(models.Model):
	owner = models.ForeignKey(User, related_name='owner', default='')
	requester = models.ForeignKey(User, related_name='requester', default='')
	description = models.CharField(max_length=45)
	time = models.DateTimeField(auto_now=True)
	priority = models.BooleanField() # True, False
	status = models.CharField(max_length=6) # open, closed