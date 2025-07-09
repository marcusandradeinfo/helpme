from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from . import form, serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from django.contrib import messages


# Create your views here.
class ChamadosList(LoginRequiredMixin, ListView):
    model = models.Chamados 
    template_name = 'chamados_list.html'
    context_object_name = 'chamados'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        numero_chamado = self.request.GET.get('numero_chamado')

        if numero_chamado:
            queryset = queryset.filter(nome__icontains=numero_chamado)

        return queryset

class ChamadosCreate(LoginRequiredMixin, CreateView):
    model = models.Chamados
    template_name = 'chamados_create.html'
    form_class = form.ChamadosForm
    success_url = reverse_lazy('chamados_list')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Chamado aberto com sucesso!')
        return response



class ChamadosDetail(LoginRequiredMixin, DetailView):
    model = models.Chamados
    template_name = 'chamados_details.html'


class ChamadosUpdate(LoginRequiredMixin, UpdateView):
    model = models.Chamados
    template_name = 'chamados_update.html'
    form_class = form.ChamadosForm
    success_url = reverse_lazy('chamados_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Chamado atualizado com sucesso!')
        return response
    
class ChamadosDelete(LoginRequiredMixin, DeleteView):
    model = models.Chamados
    template_name = 'chamados_delete.html'
    success_url = reverse_lazy('chamados_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Chamado deletado com sucesso!')
        return response

class ChamadosCreateApi(generics.ListAPIView):
    queryset = models.Chamados.objects.all()
    serializer_class = serializers.ChamadosSerializer