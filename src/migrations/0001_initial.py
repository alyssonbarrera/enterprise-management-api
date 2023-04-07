# Generated by Django 4.2 on 2023-04-07 02:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('num_projects', models.IntegerField(default=0)),
                ('num_employees', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(max_length=10, unique=True)),
                ('gender', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('has_driving_license', models.BooleanField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weekly_workload', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.department')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('required_hours', models.IntegerField()),
                ('estimated_deadline', models.DateField()),
                ('completed_hours', models.IntegerField()),
                ('last_hours_calculation_date', models.DateField(default=None, null=True)),
                ('done', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.department')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectEmployee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('employee_workload', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.project')),
            ],
            options={
                'verbose_name': 'ProjectEmployee',
                'verbose_name_plural': 'ProjectsEmployees',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='employees',
            field=models.ManyToManyField(related_name='employees_projects', through='src.ProjectEmployee', to='src.employee'),
        ),
        migrations.AddField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(related_name='employee_projects', through='src.ProjectEmployee', to='src.project'),
        ),
        migrations.AddIndex(
            model_name='department',
            index=models.Index(fields=['id'], name='department_id_index'),
        ),
        migrations.AddIndex(
            model_name='department',
            index=models.Index(fields=['name'], name='department_name_index'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['id'], name='project_id_index'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['name'], name='project_name_index'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['supervisor'], name='project_supervisor_index'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['department'], name='project_department_index'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['done'], name='project_done_index'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['id'], name='employee_id_index'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['name'], name='employee_name_index'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['cpf'], name='employee_cpf_index'),
        ),
    ]