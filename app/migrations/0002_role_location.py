# Generated by Django 4.0.4 on 2022-04-14 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
