# Generated by Django 4.2 on 2023-04-09 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0006_project_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='required_hours',
            new_name='remaining_hours',
        ),
    ]
