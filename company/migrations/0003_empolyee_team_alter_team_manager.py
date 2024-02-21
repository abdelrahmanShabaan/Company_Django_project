# Generated by Django 5.0.2 on 2024-02-21 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_team_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='empolyee',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_manager', to='company.empolyee'),
        ),
    ]
