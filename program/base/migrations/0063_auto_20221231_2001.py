# Generated by Django 3.2.7 on 2022-12-31 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0062_auto_20221231_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user6',
            name='createtime',
        ),
        migrations.RemoveField(
            model_name='user6',
            name='updatetime',
        ),
    ]
