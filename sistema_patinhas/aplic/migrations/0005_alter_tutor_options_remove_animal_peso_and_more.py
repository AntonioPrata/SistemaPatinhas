# Generated by Django 5.1.1 on 2024-10-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0004_tutor_alter_animal_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutor',
            options={'verbose_name_plural': 'Tutores'},
        ),
        migrations.RemoveField(
            model_name='animal',
            name='peso',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='CPF',
        ),
        migrations.AddField(
            model_name='tutor',
            name='cpf',
            field=models.CharField(default='00000000000', max_length=11),
        ),
    ]
