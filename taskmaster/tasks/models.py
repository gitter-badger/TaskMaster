from django.db import models

# Create your models here.
class Task(models.Model):
	name = models.CharField(max_length=30)
	date = models.DateField()
	done = False;

	def __unicode__(self):
		return self.name