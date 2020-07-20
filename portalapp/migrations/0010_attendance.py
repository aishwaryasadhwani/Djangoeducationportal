# Generated by Django 3.0.6 on 2020-07-14 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0009_studentattendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Class', models.CharField(max_length=40)),
                ('StudentName', models.CharField(max_length=255)),
                ('Status', models.CharField(max_length=20)),
            ],
        ),
    ]
