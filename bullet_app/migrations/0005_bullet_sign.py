# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bullet_app', '0004_bullet_bullet_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='bullet',
            name='sign',
            field=models.CharField(default='+', choices=[('+', '+'), ('-', '-')], max_length=1),
            preserve_default=True,
        ),
    ]
