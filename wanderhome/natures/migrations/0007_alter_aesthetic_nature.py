# Generated by Django 4.0.6 on 2022-07-26 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('natures', '0006_alter_aesthetic_nature_alter_move_id_alter_nature_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aesthetic',
            name='nature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='natures.nature'),
        ),
    ]
