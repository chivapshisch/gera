# Generated by Django 5.0.6 on 2024-08-16 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0006_remove_opisanie_adress_city_adress"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="city",
            name="adress",
        ),
    ]
