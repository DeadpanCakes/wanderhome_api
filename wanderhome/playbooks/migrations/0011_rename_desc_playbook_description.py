# Generated by Django 4.0.6 on 2022-07-29 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playbooks', '0010_rename_name_animal_text_rename_name_appearance_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playbook',
            old_name='desc',
            new_name='description',
        ),
    ]
