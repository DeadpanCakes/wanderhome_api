# Generated by Django 4.0.6 on 2022-07-29 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playbooks', '0011_rename_desc_playbook_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalityoption',
            name='personality',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='playbooks.personality'),
        ),
    ]
