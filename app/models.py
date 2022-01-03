from django.db import models

# Create your models here.

class Character(models.Model):
	name = models.TextField()
	sentiment = models.TextField()
	number_of_lines = models.TextField()

	def __str__(self):
		"""A string representation of a character."""
		return self.name

# class Line(models.Model):
# 	name = models.TextField()
# 	text = models.TextField()
# 	sentiment = models.TextField()

# 	def __str__(self):
# 		"""A string representation of a line."""
# 		return self.text