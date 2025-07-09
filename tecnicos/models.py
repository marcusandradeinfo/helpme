from django.db import models
from clientes.models import Estado, Cidade, Bairro, Nivel, StatusClientes
    
class FormacaoTecnico(models.Model):
    nome = models.CharField(max_length=200)
    class Meta:
        ordering = ['nome']
    def __str__(self):
        return self.nome


class Tecnicos(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    rg = models.CharField(null=True, blank=True, default=0)
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=200)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='estado_tecnicos')
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, related_name='cidade_tecnicos')
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT, related_name='bairro_tecnicos')
    cep = models.CharField(max_length=20)
    telefone = models.CharField(max_length=200)
    formacao = models.ForeignKey(FormacaoTecnico, on_delete=models.PROTECT, related_name='formacao_tecnicos')
    status = models.ForeignKey(StatusClientes, on_delete=models.PROTECT, related_name='status_tecnicos')
    nivel = models.ForeignKey(Nivel, on_delete=models.PROTECT, related_name='nivel_tecnicos')
    n3 = models.IntegerField(null=True, blank=True, default=0)
    n2 = models.IntegerField(null=True, blank=True, default=0)
    n1 = models.IntegerField(null=True, blank=True, default=0)
    observacao = models.CharField(max_length=200, null=True, blank=True)
        
    class Meta:
        ordering = ['nome']
        
    def __str__(self):
        return self.nome
