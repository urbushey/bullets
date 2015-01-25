# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bullet_app', '0005_bullet_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bullet',
            name='text',
            field=models.TextField(),
        ),
    ]
