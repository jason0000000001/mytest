# Generated by Django 3.2.7 on 2022-12-31 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0066_auto_20221231_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(default=True)),
                ('temperature', models.FloatField(default=True)),
                ('pressures', models.IntegerField(default=True)),
                ('pressured', models.IntegerField(default=True)),
                ('bmi', models.FloatField(default=0.0)),
                ('bmr', models.FloatField(default=0.0)),
                ('result1', models.CharField(default=True, max_length=100)),
                ('result2', models.CharField(default=True, max_length=100)),
                ('result3', models.CharField(default=True, max_length=100)),
                ('updatetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User7',
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
            name='Data6',
        ),
        migrations.DeleteModel(
            name='User6',
        ),
        migrations.AddField(
            model_name='data7',
            name='userid',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='base.user7'),
        ),
    ]
