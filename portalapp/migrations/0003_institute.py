# Generated by Django 3.0.6 on 2020-06-15 10:50

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0002_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InstituteName', models.CharField(max_length=255)),
                ('TargetLine', models.CharField(max_length=255)),
                ('InstituteLogo', models.FileField(upload_to='images/')),
                ('Phone', models.IntegerField()),
                ('Website', models.CharField(max_length=255)),
                ('InstituteAddress', models.CharField(max_length=255)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
    ]