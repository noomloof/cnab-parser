# Generated by Django 4.1.3 on 2022-11-21 15:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=90)),
                ('business_name', models.CharField(max_length=200)),
            ],
        ),
    ]
