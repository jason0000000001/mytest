# Generated by Django 3.2.7 on 2022-12-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_data1_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data1',
            name='name',
        ),
        migrations.AddField(
            model_name='data1',
            name='userid',
            field=models.IntegerField(db_column='userid', default=True),
        ),
    ]
