# Generated by Django 4.0.5 on 2022-08-26 04:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0002_alter_editor_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editor',
            name='Description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
