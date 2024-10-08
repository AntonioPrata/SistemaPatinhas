from django.db import models


class SexOptions(models.TextChoices):
    FEMALE = 'F', 'Femêa'
    MALE = 'M', 'Macho'


class Raca(models.Model):
    nome_raca = models.CharField(("Raça"), max_length=50, blank=True, null=False)
    descricao_raca = models.TextField()

    class Meta:
        verbose_name_plural = 'Raças'

    def str(self):
        return self.nome_raca


class Animal(models.Model):
    nome = models.CharField(max_length=50)
    peso = models.FloatField(('peso'), blank=True, null=True, max_length="5")
    data_nascimento = models.DateField(max_length=8, blank=True, null=True)
    sexo = models.CharField(('sexo'), max_length=1, choices=SexOptions.choices)
    personalidade = models.CharField()
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE, null=True)


class Cachorro(Animal):
    porte = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Cachorros'

    def str(self):
        return self.nome


class Gato(Animal):
    class Meta:
        verbose_name_plural = 'Gatos'

    def str(self):
        return self.nome


class Tutor(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(('CPF'), max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(max_length=8, blank=True, null=True)
    telefone = models.CharField(('Telefone'), max_length=11, blank=True, null=True)
    email = models.EmailField(('Email'), blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Tutores'

    def str(self):
        return self.nome

class Tipo(models.Model):
    nome_tipo = models.CharField(("Tipo"), max_length=50)
    descricao_tipo = models.TextField('Descrição')

    class Meta:
        verbose_name_plural = 'Tipos'

    def str(self):
        return self.nome_tipo

class Evento(models.Model):
    data_inicio = models.DateField(('Data Início'), max_length=8, blank=True, null=True)
    data_fim = models.DateField(('Data Fim'),max_length=8, blank=True, null=True)
    descricao = models.CharField(('Descrição do Evento'), max_length=50)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Eventos'

    class Meta:
        verbose_name_plural = 'Tipos'

    def str(self):
        return self.nome_tipo

