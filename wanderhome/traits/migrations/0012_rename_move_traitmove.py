# Generated by Django 4.0.6 on 2022-07-27 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0002_alter_option_id_alter_option_non_magic_text_and_more'),
        ('traits', '0011_alter_move_trait_alter_trait_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Move',
            new_name='TraitMove',
        ),
    ]