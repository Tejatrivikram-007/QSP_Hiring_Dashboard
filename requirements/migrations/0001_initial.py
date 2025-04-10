# Generated by Django 5.2 on 2025-04-09 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=100)),
                ('bachelor_degree', models.CharField(max_length=100)),
                ('master_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('stream', models.CharField(max_length=100)),
                ('year_of_passout', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('no_of_vacancies', models.IntegerField()),
                ('salary', models.CharField(blank=True, max_length=100, null=True)),
                ('agreement', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
