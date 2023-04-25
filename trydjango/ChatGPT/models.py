from django.db import models


# Create your models here.
class ChatGPT(models.Model):
	title =  models.TextField()
	description = models.TextField()

