# Generated by Django 5.0.2 on 2024-07-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='intern',
            field=models.BooleanField(null=True),
        ),
    ]
