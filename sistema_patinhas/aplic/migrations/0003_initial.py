# Generated by Django 5.1.1 on 2024-10-03 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aplic', '0002_delete_animal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('peso', models.FloatField()),
                ('raca', models.CharField(max_length=25)),
            ],
        ),
    ]
