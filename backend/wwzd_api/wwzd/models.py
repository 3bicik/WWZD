from django.db import models

# Create your models here.

class Character(models.Model):
	name = models.TextField()
	personality = models.TextField()

	def __str__(self):
		"""A string representation of a character."""
		return self.name

class Line(models.Model):

	text = models.TextField()
	emotion = models.TextField()

	def __str__(self):
		"""A string representation of a line."""
		return self.text
