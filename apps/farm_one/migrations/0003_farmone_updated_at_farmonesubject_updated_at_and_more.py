# Generated by Django 4.2.4 on 2023-09-23 05:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("farm_one", "0002_rename_turbidity_farmone_humidity_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="farmone",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="farmonesubject",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="subject",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]