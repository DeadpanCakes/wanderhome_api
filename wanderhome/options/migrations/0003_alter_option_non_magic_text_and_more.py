# Generated by Django 4.0.6 on 2022-07-30 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0002_alter_option_id_alter_option_non_magic_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='non_magic_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='option',
            name='non_traumatized_or_magic_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='option',
            name='non_traumatized_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
