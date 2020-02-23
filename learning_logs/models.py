from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	'''A theme that user investigate'''
	text = models.CharField(max_length=250)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		'''returns string form of model'''
		return self.text

class Entry(models.Model):
	'''Information investigated by user on the topic'''
	topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		'''returns string form of model'''
		return self.text[:50] + '...'