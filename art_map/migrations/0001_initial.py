# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtPiece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, null=True)),
                ('description', models.CharField(max_length=2048, null=True)),
                ('photoURL', models.CharField(max_length=256, null=True)),
                ('lat', models.FloatField(null=True)),
                ('lon', models.FloatField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
