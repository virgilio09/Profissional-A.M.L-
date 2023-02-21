from django.contrib.auth.models import User
from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=9, null=False, blank=False, verbose_name='CEP')
    rua = models.CharField(max_length=200, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.rua

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome

class Servico(models.Model):

    STATUS = (
        ('ativo', 'Ativo'),
        ('desativado', 'Desativado'),
    )
   
    nome = models.CharField(max_length=50)
    user = models.ForeignKey(User,  on_delete=models.CASCADE, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    status = models.CharField(
        max_length=10,
        choices=STATUS,
    )
    capa = models.ImageField(null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    telefone01 = models.CharField(max_length=15, blank=False, null=False, verbose_name='Telefone 1')
    telefone02 = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefone 2 (Opcional)')
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=False)
    descricao = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Imagem(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, verbose_name='Adicione images do seu serviço')

    def __str__(self):
        return self.servico.nome


class Comment(models.Model):
    STATUS = (
        ('Lido', 'Lido'),
        ('Não Lido', 'Não Lido'),
    )
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)

    nome = models.CharField(max_length=50, blank=False)
    comment = models.TextField()

    status = models.CharField(choices=STATUS, max_length=10, default="Não Lido")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
   
class Help(models.Model):
    titulo = models.CharField(max_length=100)
    text =  models.TextField()

    def __str__(self):
        return self.titulo
