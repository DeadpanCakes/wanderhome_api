# Generated by Django 4.0.6 on 2022-07-29 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natures', '0010_rename_prompt_naturemove_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='nature',
            name='description',
            field=models.CharField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]