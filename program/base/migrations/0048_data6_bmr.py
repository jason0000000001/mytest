# Generated by Django 3.2.7 on 2022-12-30 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0047_auto_20221230_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='data6',
            name='bmr',
            field=models.FloatField(default=0.0),
        ),
    ]
