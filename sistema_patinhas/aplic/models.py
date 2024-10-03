from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=50)
    peso = models.FloatField()
    data_nascimento = models.DateField
    raca = models.CharField(max_length=25)
    class Meta:
        verbose_name_plural = 'Animais'

    def __str__(self):
        
        return self.nome
    
class Tutor(models.Model):
    CPF = models.FloatField(10)
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField
    class Meta:
        verbose_name_plural = 'Tutores'
    
    def __str__(self):
        
        return self.nome



