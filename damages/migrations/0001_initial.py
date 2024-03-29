# Generated by Django 2.2.6 on 2019-10-10 07:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Damage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_incident', models.DateField()),
                ('call_number', models.IntegerField()),
                ('customer', models.CharField(max_length=50)),
                ('vehicle_year', models.IntegerField()),
                ('vehicle_make', models.CharField(max_length=50)),
                ('vehicle_model', models.CharField(max_length=50)),
                ('damages', models.TextField()),
                ('status', models.CharField(max_length=100)),
                ('cost', models.IntegerField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('date_resolved', models.DateField(blank=True)),
                ('is_open', models.BooleanField(default=True)),
                ('image_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_8', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('entry_date', models.DateTimeField(default=datetime.datetime.now)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employees.Employees')),
            ],
        ),
    ]
