# Generated by Django 2.2.6 on 2019-10-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('citystate', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('cell', models.CharField(max_length=200)),
                ('cdl', models.CharField(max_length=200)),
                ('hite_date', models.DateField()),
                ('er_contact', models.CharField(max_length=200)),
                ('er_number', models.CharField(max_length=200)),
            ],
        ),
    ]
