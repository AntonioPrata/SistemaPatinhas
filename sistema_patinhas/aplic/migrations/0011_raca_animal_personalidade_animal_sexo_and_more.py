# Generated by Django 5.1.1 on 2024-10-06 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0010_animal_data_nascimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_raca', models.CharField(max_length=50)),
                ('descricao_raca', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='personalidade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='sexo',
            field=models.CharField(blank=True, choices=[('F', 'Femêa'), ('M', 'Macho')], max_length=1, null=True, verbose_name='sexo'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='data_nascimento',
            field=models.DateField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='telefone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefone'),
        ),
        migrations.AddField(
            model_name='cachorro',
            name='raca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.raca'),
        ),
    ]
