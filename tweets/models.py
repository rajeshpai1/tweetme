from django.db import models

# Create your models here.

class Tweets(models.Model):
  content = models.TextFeild(blank = True, null= True)
  image = models.FileFeild(uplaod_to='images', blank=True)
