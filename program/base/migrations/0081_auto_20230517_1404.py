# Generated by Django 3.2.7 on 2023-05-17 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0080_rename_user_medicine_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='medicine',
            new_name='describe',
        ),
        migrations.AddField(
            model_name='medicine',
            name='dose',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='name',
            field=models.TextField(null=True),
        ),
    ]
