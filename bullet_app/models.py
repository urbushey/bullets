from django.db import models


# Create your models here.
class Bullet(models.Model):

    text = models.TextField(default='')
