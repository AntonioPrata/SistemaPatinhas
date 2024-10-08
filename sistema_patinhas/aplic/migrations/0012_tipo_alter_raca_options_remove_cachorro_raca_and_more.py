
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0011_raca_animal_personalidade_animal_sexo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tipo', models.CharField(max_length=50, verbose_name='Tipo')),
                ('descricao_tipo', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.AlterModelOptions(
            name='raca',
            options={'verbose_name_plural': 'Raças'},
        ),
        migrations.RemoveField(
            model_name='cachorro',
            name='raca',
        ),
        migrations.AddField(
            model_name='animal',
            name='raca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.raca'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='personalidade',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('F', 'Femêa'), ('M', 'Macho')], max_length=1, verbose_name='sexo'),
        ),
        migrations.AlterField(
            model_name='raca',
            name='descricao_raca',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='raca',
            name='nome_raca',
            field=models.CharField(blank=True, max_length=50, verbose_name='Raça'),
        ),

        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(blank=True, max_length=8, null=True, verbose_name='Data Início')),
                ('data_fim', models.DateField(blank=True, max_length=8, null=True, verbose_name='Data Fim')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição do Evento')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.tipo')),
            ],
            options={
                'verbose_name_plural': 'Eventos',
            },
        )
        ]

