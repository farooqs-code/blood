# Generated by Django 2.2.6 on 2019-12-08 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=30)),
                ('password', models.TextField(max_length=14)),
                ('age', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=300)),
                ('blood_group', models.TextField()),
                ('address', models.TextField()),
                ('Last_donoted_date', models.DateField()),
            ],
        ),
    ]