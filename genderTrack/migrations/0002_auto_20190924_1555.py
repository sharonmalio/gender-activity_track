# Generated by Django 2.1.11 on 2019-09-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genderTrack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
