from django.db import models
from addon.fields import JSONField

# Create your models here.
class Addon(models.Model):
	name = models.CharField(max_length=30, unique=True)
	config_vars = JSONField(default='')
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	class Meta: 
		ordering = ["name"]

	def __unicode__(self):
		return self.name
