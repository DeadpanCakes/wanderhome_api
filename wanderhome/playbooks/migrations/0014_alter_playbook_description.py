# Generated by Django 4.0.6 on 2022-07-31 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playbooks', '0013_alter_personality_playbook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playbook',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]