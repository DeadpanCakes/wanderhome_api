# Generated by Django 4.0.6 on 2022-07-23 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playbooks', '0003_alter_appearance_name_alter_personalityoption_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personality',
            old_name='personality_prompt',
            new_name='prompt',
        ),
    ]
