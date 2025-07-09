from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.dados import DadosChamados


@login_required(login_url='login')
def home(request):
    valores_chamados, dados_chamados = DadosChamados()

    context = {'valores_chamados': valores_chamados,
               'dados_chamados': dados_chamados, }

    return render(request, 'home.html', context)
