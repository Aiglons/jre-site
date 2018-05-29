# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-29 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import precise_bbcode.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='_text_rendered',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=precise_bbcode.fields.BBCodeTextField(no_rendered_field=True),
        ),
    ]