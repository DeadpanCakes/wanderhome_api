# Generated by Django 4.0.6 on 2022-08-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0008_alter_custom_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='description',
            field=models.CharField(max_length=600),
        ),
    ]
