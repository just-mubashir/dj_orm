# Generated by Django 4.0.4 on 2022-04-14 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_employee_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='bonous',
            new_name='incentives',
        ),
    ]
