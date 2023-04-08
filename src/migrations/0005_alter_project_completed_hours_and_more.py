# Generated by Django 4.2 on 2023-04-07 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_alter_employee_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='completed_hours',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='employees',
            field=models.ManyToManyField(blank=True, related_name='employees_projects', through='src.ProjectEmployee', to='src.employee'),
        ),
        migrations.AlterField(
            model_name='project',
            name='estimated_deadline',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='required_hours',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='src.employee'),
        ),
    ]
