# Generated by Django 3.2.7 on 2022-10-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20221024_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='room',
            name='pressured',
        ),
        migrations.RemoveField(
            model_name='room',
            name='pressures',
        ),
        migrations.RemoveField(
            model_name='room',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='room',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='room',
            name='weight',
        ),
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
