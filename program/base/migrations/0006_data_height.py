# Generated by Django 3.2.7 on 2022-10-25 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_room_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='height',
            field=models.FloatField(default=True),
        ),
    ]