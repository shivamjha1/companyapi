# Generated by Django 5.0.2 on 2024-07-02 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('post', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
