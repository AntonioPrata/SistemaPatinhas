# Generated by Django 5.1.1 on 2024-10-03 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0005_alter_tutor_options_remove_animal_peso_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='peso',
            field=models.FloatField(blank=True, max_length='5', null=True, verbose_name='peso'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF'),
        ),
    ]
