# Generated by Django 3.2.7 on 2022-12-30 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0046_data6_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data6',
            old_name='result',
            new_name='result1',
        ),
        migrations.AddField(
            model_name='data6',
            name='result2',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='data6',
            name='result3',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
