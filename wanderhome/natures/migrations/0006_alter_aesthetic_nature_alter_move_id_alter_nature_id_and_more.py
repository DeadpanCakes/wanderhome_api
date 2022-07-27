# Generated by Django 4.0.6 on 2022-07-26 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('natures', '0005_rename_category_naturecategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aesthetic',
            name='nature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='natures.nature', unique=True),
        ),
        migrations.AlterField(
            model_name='move',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nature',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nature',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='naturecategory',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='naturecategory',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]