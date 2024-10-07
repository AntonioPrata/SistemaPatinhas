
from django.db import models

class SexOptions(models.TextChoices):
    FEMALE = 'F', 'Femêa'
    MALE = 'M', 'Macho'

class Animal(models.Model):
    nome = models.CharField(max_length=50)
    peso = models.FloatField(('peso'), blank=True, null=True, max_length="5")
    data_nascimento = models.DateField(max_length=8 ,blank=True, null=True)
    sexo = models.CharField(('sexo'), max_length=1, choices=SexOptions.choices)
    personalidade = models.CharField()

class Raca(models.Model):
    nome_raca = models.CharField(max_length=50)
    descricao_raca = models.TextField()

class Cachorro(Animal):
    porte = models.CharField(max_length=50)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cachorros'

    def __str__(self):
        return self.nome

class Gato(Animal):
    class Meta:
        verbose_name_plural = 'Gatos'

    def __str__(self):
        
        return self.nome
    
class Tutor(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(('CPF'),max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(max_length=8 ,blank=True, null=True)
    telefone = models.CharField(('Telefone'), max_length=11, blank=True, null=True)
    email = models.EmailField(('Email'), blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Tutores'
    
    def __str__(self):
        
        return self.nome

    



