from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	Title = models.CharField(max_length=100)
	Content = models.TextField()
	Date_posted = models.DateTimeField(default=timezone.now)
	Author = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
	 return self.Title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk' : self.pk})
