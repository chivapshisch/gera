# Generated by Django 5.0.6 on 2024-08-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0005_city_remove_names_adress_opisanie_adress_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="opisanie",
            name="adress",
        ),
        migrations.AddField(
            model_name="city",
            name="adress",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
