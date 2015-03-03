# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bullet_app', '0007_auto_20150302_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bullet',
            name='original_text',
            field=models.TextField(blank=True),
        ),
    ]
