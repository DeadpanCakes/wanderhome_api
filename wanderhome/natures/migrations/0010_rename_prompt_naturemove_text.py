# Generated by Django 4.0.6 on 2022-07-29 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('natures', '0009_alter_aesthetic_nature_alter_lore_nature_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='naturemove',
            old_name='prompt',
            new_name='text',
        ),
    ]