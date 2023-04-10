# Generated by Django 4.2 on 2023-04-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0007_rename_required_hours_project_remaining_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='projectemployee',
            name='role',
            field=models.CharField(default='employee', max_length=100, null=True),
        ),
    ]
