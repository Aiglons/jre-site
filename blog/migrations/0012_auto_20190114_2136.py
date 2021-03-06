# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-14 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20181005_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='color',
            field=models.CharField(help_text='Consultez la liste des couleur possible <a href="../../../../../documentation#color">ici</a>', max_length=30),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='icon',
            field=models.CharField(help_text='Consultez la liste des logo possible <a href="../../../../../documentation#Icon">ici</a>', max_length=30),
        ),
    ]
