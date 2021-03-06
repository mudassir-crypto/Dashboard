# Generated by Django 3.2.7 on 2021-09-18 07:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('language', models.CharField(blank=True, choices=[('English', 'English'), ('Hindi', 'Hindi')], max_length=200, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('qualification', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('standard', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('course_enrolled', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.teacher'),
        ),
    ]
