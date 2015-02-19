from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

class BulletGroup(models.Model):

    def get_absolute_url(self):
        return reverse('view_bullets', args=[self.id])


class Bullet(models.Model):

    text = models.TextField(blank=False)
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
