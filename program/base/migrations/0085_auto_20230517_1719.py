# Generated by Django 3.2.7 on 2023-05-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0084_auto_20230517_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='hour',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='min',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
