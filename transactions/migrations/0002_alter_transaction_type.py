# Generated by Django 4.1.3 on 2022-11-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="type",
            field=models.CharField(
                choices=[("Entrada", "Income"), ("Saida", "Outcome")],
                default="Entrada",
                max_length=10,
            ),
        ),
    ]
