# Generated by Django 3.2.7 on 2022-12-29 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_alter_data6_bmi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='x',
            new_name='bmi',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='y',
            new_name='height',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='z',
            new_name='weight',
        ),
    ]