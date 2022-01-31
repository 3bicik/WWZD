from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Character(models.Model):
	name = models.TextField()
	data = models.TextField()
	number_of_lines = models.TextField()

	def __str__(self):
		"""A string representation of a character."""
		return self.name
