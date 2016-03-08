from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	"""This model will represent a Post object in the application"""

	def __str__(self):
		return "post(pk={0}) >>> \"{1}\"".format(self.id, self.title)

	author = models.ForeignKey(User)
	title = models.CharField(max_length=200, blank=False)
	date = models.DateTimeField(auto_now_add=True, blank=False)
	text = models.TextField(blank=False)

class Link(models.Model):
	"""This model will represent a Link object in the application"""

	def __str__(self):
		return "link(pk={0}) >>> \"{1}\"".format(self.id, self.title)

	post = models.ForeignKey(Post)
	url = models.URLField(max_length=350, blank=False)
	title = models.CharField(max_length=200, blank=False)

class Profile(models.Model):
	"""This model will represent a Profile for each User in the applicaiton."""

	def __str__(self):
		return "profile(pk={0})".format(self.id)

	bio = models.TextField(blank=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
