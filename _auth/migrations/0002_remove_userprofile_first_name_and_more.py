# Generated by Django 4.0.4 on 2022-05-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='iin',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='reader_id',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]