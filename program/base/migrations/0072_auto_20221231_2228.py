# Generated by Django 3.2.7 on 2022-12-31 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0071_auto_20221231_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='data6',
            name='createtime',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 12, 31, 14, 28, 7, 950070, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user6',
            name='createtime',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 12, 31, 14, 28, 29, 312821, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user6',
            name='updatetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]