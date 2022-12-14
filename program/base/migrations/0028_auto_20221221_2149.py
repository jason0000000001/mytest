# Generated by Django 3.2.7 on 2022-12-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_auto_20221221_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data0',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('weight', models.FloatField(default=True)),
                ('temperature', models.FloatField(default=True)),
                ('pressures', models.IntegerField(db_column='pressureS')),
                ('pressured', models.IntegerField(db_column='pressureD')),
            ],
        ),
        migrations.CreateModel(
            name='User0',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.IntegerField(db_column='imageid')),
                ('name', models.CharField(max_length=45)),
                ('birthday', models.CharField(default=True, max_length=45)),
                ('sex', models.CharField(default=True, max_length=45)),
                ('height', models.FloatField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Data5',
        ),
        migrations.DeleteModel(
            name='User5',
        ),
    ]
