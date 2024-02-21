# Generated by Django 5.0.2 on 2024-02-21 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_manager', to='company.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.team'),
        ),
    ]
