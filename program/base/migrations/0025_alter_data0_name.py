# Generated by Django 3.2.7 on 2022-12-18 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_auto_20221215_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data0',
            name='name',
            field=models.CharField(max_length=45),
        ),
    ]
