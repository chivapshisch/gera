# Generated by Django 5.0.6 on 2024-08-22 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0015_delete_mnenie"),
        ("ocenki", "0004_alter_mnenie_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mnenie",
            name="name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="nnn",
                to="index.names",
            ),
        ),
    ]
