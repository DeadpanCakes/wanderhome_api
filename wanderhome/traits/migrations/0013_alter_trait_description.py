# Generated by Django 4.0.6 on 2022-07-31 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0012_rename_move_traitmove'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trait',
            name='description',
            field=models.CharField(max_length=400, unique=True),
        ),
    ]