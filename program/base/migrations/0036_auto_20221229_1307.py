# Generated by Django 3.2.7 on 2022-12-29 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0035_auto_20221229_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='bmi',
            new_name='x',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='height',
            new_name='y',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='weight',
            new_name='z',
        ),
    ]
