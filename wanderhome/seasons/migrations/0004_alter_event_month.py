# Generated by Django 4.0.6 on 2022-07-31 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0003_holiday_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='month',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='seasons.month'),
        ),
    ]
