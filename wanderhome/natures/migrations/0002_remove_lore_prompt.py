# Generated by Django 4.0.6 on 2022-07-23 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('natures', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lore',
            name='prompt',
        ),
    ]
