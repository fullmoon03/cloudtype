# Generated by Django 4.2.7 on 2023-12-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bsk_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flowerpot",
            name="pot_number",
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]