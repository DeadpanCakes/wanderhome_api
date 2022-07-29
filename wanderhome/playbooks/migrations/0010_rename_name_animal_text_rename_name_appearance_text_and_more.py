# Generated by Django 4.0.6 on 2022-07-29 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playbooks', '0009_alter_animal_id_alter_animal_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='appearance',
            old_name='name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='personalityoption',
            old_name='name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='relationship',
            old_name='prompt',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='seasonalmove',
            old_name='name',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='signaturemove',
            old_name='name',
            new_name='text',
        ),
    ]
