from django.db import models
from djangotoolbox.fields import ListField
#from mongoapp.forms import StringListField
# Create your models here.
"""
class CategoryField(ListField):
	def formfield(self, **kwargs):
		return models.Field.formfield(self, StringListField, **kwargs)
"""
class Create(models.Model):
	FirstName = models.CharField(max_length=255)
	LastName = models.CharField(max_length=255)
	Email = models.EmailField()
	comments = ListField(null=True)

	def __unicode__(self):
		return self.FirstName

class CreateUser(models.Model):
	FiestName = models.CharField(max_length=255)
	#comments = ListField(null=True)