# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bullet_app', '0003_bulletgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='bullet',
            name='bullet_group',
            field=models.ForeignKey(to='bullet_app.BulletGroup', default=None),
            preserve_default=True,
        ),
    ]
