# Generated by Django 4.0.6 on 2022-07-27 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0006_alter_trait_description_alter_trait_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trait',
            name='category',
        ),
        migrations.AddField(
            model_name='traitcategory',
            name='traits',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='traits.trait'),
            preserve_default=False,
        ),
    ]
