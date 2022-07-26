# Generated by Django 4.0.6 on 2022-07-22 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0001_initial'),
        ('traits', '0002_remove_trait_options_trait_moves_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trait',
            name='moves',
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('option_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='options.option')),
                ('trait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traits.trait')),
            ],
            bases=('options.option',),
        ),
    ]
