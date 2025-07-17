from chamados.models import Chamados
from tecnicos.models import Tecnicos


def DadosChamados():
    chamados_atendidos = Chamados.objects.filter(status__status__iexact='fechado').count()
    chamados_abertos = Chamados.objects.filter(status__status__iexact='aberto').count()
    tecnicos_disponiveis = Tecnicos.objects.filter(status__status__iexact='ativo').count()
    queryset = Chamados.objects.filter(
        status__status__iexact='Aberto'
    ).order_by('-numero_chamado')[:3]  # Tenta pegar no máximo 3, mesmo que só exista 1
    chamados_dados = []
    for chamado in queryset:
        chamados_dados.append({
            'NumeroChamado': chamado.numero_chamado,
            'Cliente': chamado.cliente,
            'Tecnicos': chamado.tecnicos,
            'DataAtendimento': chamado.data_atendimento,
            'HorarioAtendimento': chamado.horario_atendimento,
        })
    valores_chamados = dict(chamados_atendidos = chamados_atendidos,
                chamados_abertos = chamados_abertos,
                tecnicos_disponiveis = tecnicos_disponiveis,
                )
    dados_chamados = chamados_dados
    return  valores_chamados, dados_chamados
