from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from . import form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages



# Create your views here.
class ClientesList(LoginRequiredMixin, ListView):
    model = models.Clientes
    template_name = 'clientes_list.html'
    context_object_name = 'clientes'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        nome_cliente = self.request.GET.get('nome')

        if nome_cliente:
            queryset = queryset.filter(nome__icontains=nome_cliente)

        return queryset
    


class ClientesCreate(LoginRequiredMixin, CreateView):
    model = models.Clientes
    template_name = 'clientes_create.html'
    form_class = form.ClientesForm
    success_url = reverse_lazy('clientes_list')
        
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cliente cadastrado com sucesso!')
        return response


class ClientesDetail(LoginRequiredMixin, DetailView):
    model = models.Clientes
    template_name = 'clientes_details.html'

class ClientesUpdate(LoginRequiredMixin, UpdateView):
    model = models.Clientes
    template_name = 'clientes_update.html'
    form_class = form.ClientesForm
    success_url = reverse_lazy('clientes_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Dados do cliente atualizados com sucesso!')
        return response    
    
class ClientesDelete(LoginRequiredMixin, DeleteView):
    model = models.Clientes
    template_name = 'clientes_delete.html'
    success_url = reverse_lazy('clientes_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Chamado excluído com sucesso!')
        return response