# Generated by Django 3.2.7 on 2022-12-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20221209_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user1',
            name='weight',
        ),
        migrations.AddField(
            model_name='data1',
            name='weight',
            field=models.FloatField(default=True),
        ),
    ]
