# Generated by Django 3.2.7 on 2022-12-29 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0040_remove_data6_names'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data6',
            old_name='name',
            new_name='userid',
        ),
    ]