# Generated by Django 3.2.7 on 2022-12-31 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0069_auto_20221231_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data7',
            name='updatetime',
        ),
    ]