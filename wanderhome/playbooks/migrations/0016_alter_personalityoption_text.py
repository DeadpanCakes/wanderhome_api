# Generated by Django 4.0.6 on 2022-07-31 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playbooks', '0015_alter_seasonalmove_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalityoption',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]
