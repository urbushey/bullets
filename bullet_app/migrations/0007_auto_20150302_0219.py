# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bullet_app', '0006_auto_20150112_0600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bullet',
            name='sign',
        ),
        migrations.AddField(
            model_name='bullet',
            name='negative_score',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bullet',
            name='original_text',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bullet',
            name='positive_score',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
