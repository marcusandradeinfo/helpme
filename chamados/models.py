from django.db import models
from clientes.models import Estado, Cidade, Bairro, Nivel
from tecnicos.models import Tecnicos

class StatusChamados(models.Model):
    status = models.CharField(max_length=30)
    class Meta:
        ordering = ['status']
        
    def __str__(self):
        return str(self.status)


class Chamados(models.Model):
    numero_chamado = models.AutoField(primary_key=True)
    cliente =models.CharField(max_length=200)
    endereco =models.CharField(max_length=200)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, related_name='cidade_chamado')
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='estado_chamado')
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT, related_name='bairro_chamado')    
    telefone = models.CharField(max_length=200)
    tecnicos = models.ForeignKey(Tecnicos, null=True, blank=True, on_delete=models.SET_NULL, related_name='tecnicos_chamado')    
    data_abertura = models.DateTimeField(auto_now=True)
    data_atendimento =  models.DateField()
    horario_atendimento = models.TimeField()
    status = models.ForeignKey(StatusChamados, on_delete=models.PROTECT, related_name='status_chamado')
    nivel = models.ForeignKey(Nivel, on_delete=models.PROTECT, related_name='nivel_chamado')
    motivo = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['data_atendimento']     
    def __str__(self):
        return str(self.numero_chamado)
    