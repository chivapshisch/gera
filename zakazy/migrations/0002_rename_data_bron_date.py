# Generated by Django 5.0.6 on 2024-08-17 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("zakazy", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bron",
            old_name="data",
            new_name="date",
        ),
    ]
