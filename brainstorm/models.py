from django.db import models
from django.contrib.auth.models import User

"""
class User(models.Model):
	uname = models.CharField(max_length=50)
	pword = models.CharField(max_length=250)
	join_date = models.DateTimeField('date created')
	def __unicode__(self):
		return self.uname
"""

class Topic(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	author = models.ForeignKey(User)
	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()
	def __unicode__(self):
		return self.title


class Response(models.Model):
	text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	author = models.ForeignKey(User)
	topic = models.ForeignKey(Topic)
	def __unicode__(self):
		return self.text
