from django.db import models


# Create your models here.

class BulletGroup(models.Model):
    pass


class Bullet(models.Model):

    text = models.TextField(default='')
    bullet_group = models.ForeignKey(BulletGroup, default=None)
