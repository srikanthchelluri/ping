from django.contrib.auth.models import User
from django.db import models
import datetime, random
from django.template.defaultfilters import slugify

# add ping count to User

prefix_list = ['ring-a-ding-ping', 'bells-are-pinging', 'ping-i-licious']

class Ping(models.Model):
	owner = models.ForeignKey(User, related_name='owner', default='')
	requester = models.ForeignKey(User, related_name='requester', default='')
	description = models.CharField(max_length=45)
	time = models.DateTimeField(auto_now=True)
	priority = models.BooleanField() # True, False
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		if not self.id:
			get_slug = slugify(hash(datetime.datetime.now()))
			if get_slug[0] == '-':
				self.slug = random.choice(prefix_list) + get_slug
			else:
				self.slug = random.choice(prefix_list) + "-" + get_slug
		super(Ping, self).save(*args, **kwargs)