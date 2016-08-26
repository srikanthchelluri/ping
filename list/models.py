from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Ping(models.Model):
	owner = models.ForeignKey(User, related_name='owner', default='')
	requester = models.ForeignKey(User, related_name='requester', default='')
	description = models.TextField()
	time = models.DateTimeField(auto_now=True)
	priority = models.CharField(max_length=6) # low, normal, high
	status = models.CharField(max_length=6) # open, closed