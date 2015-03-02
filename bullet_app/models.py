from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

class BulletGroup(models.Model):

    def get_absolute_url(self):
        return reverse('view_bullets', args=[self.id])


class Bullet(models.Model):

    text = models.TextField(blank=False)
    bullet_group = models.ForeignKey(BulletGroup, default=None)
    original_text = models.TextField(null=True)
    positive_score = models.SmallIntegerField(null=False, default=0)
    negative_score = models.SmallIntegerField(null=False, default=0)
