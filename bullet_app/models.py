from django.db import models


# Create your models here.

class BulletGroup(models.Model):
    pass


class Bullet(models.Model):

    text = models.TextField(default='')
    bullet_group = models.ForeignKey(BulletGroup, default=None)
    # Constants for sign option
    POS = '+'
    NEG = '-'
    SIGN_CHOICES = (
        (POS, '+'),
        (NEG, '-'),
    )
    sign = models.CharField(max_length=1,
                            choices=SIGN_CHOICES,
                            default=POS)
