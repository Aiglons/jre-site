# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-10-05 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_descriptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='color',
            field=models.CharField(default=1, help_text='COnsultez la liste des couleur possible ici ', max_length=30),
            preserve_default=False,
        ),
    ]
