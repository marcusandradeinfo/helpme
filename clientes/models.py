from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=200)    
    class Meta:
        ordering = ['nome']        
    def __str__(self):
        return self.nome

class Estado(models.Model):
    nome = models.CharField(max_length=200)
    class Meta:
        ordering = ['nome']       
    def __str__(self):
        return self.nome
    
class Bairro(models.Model):
    nome = models.CharField(max_length=200)
    class Meta:
        ordering = ['nome']
    def __str__(self):
        return self.nome


class Nivel(models.Model):
    nivel = models.IntegerField()
    class Meta:
        ordering = ['nivel']
    def __str__(self):
        return str(self.nivel)
    
class StatusClientes(models.Model):
    status = models.CharField(max_length=20)
    class Meta:
        ordering = ['status']
    def __str__(self):
        return self.status

class Clientes(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='estado_cliente')
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, related_name='cidade_cliente')
    bairro = models.ForeignKey(Bairro, on_delete=models.PROTECT, related_name='bairro_cliente')
    cep = models.CharField(max_length=20)
    telefone = models.CharField(max_length=200)
    qtd_equipamentos = models.IntegerField(null=True, blank=True, default=0)
    detalhe_equipamento = models.CharField(max_length=200)
    nivel =  models.ForeignKey(Nivel, on_delete=models.PROTECT, related_name='nivel_cliente')
    qtd_chamados = models.IntegerField(null=True, blank=True, default=0)
    status = models.ForeignKey(StatusClientes, on_delete=models.PROTECT, related_name='statuscliente_cliente')
    class Meta:
        ordering = ['nome']
    def __str__(self):
        return self.nome