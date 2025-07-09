from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from . import form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


# Create your views here.
class TecnicosList(LoginRequiredMixin, ListView):
    model = models.Tecnicos
    template_name = 'tecnicos_list.html'
    context_object_name = 'tecnicos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        nome_tecnico = self.request.GET.get('nome')

        if nome_tecnico:
            queryset = queryset.filter(nome__icontains=nome_tecnico)

        return queryset

class TecnicosCreate(LoginRequiredMixin, CreateView):
    model = models.Tecnicos
    template_name = 'tecnicos_create.html'
    form_class = form.TecnicosForm
    success_url = reverse_lazy('tecnicos_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Técnico cadastrado com sucesso!')
        return response

class TecnicosDetail(LoginRequiredMixin, DetailView):
    model = models.Tecnicos
    template_name = 'tecnicos_details.html'

class TecnicosUpdate(LoginRequiredMixin, UpdateView):
    model = models.Tecnicos
    template_name = 'tecnicos_update.html'
    form_class = form.TecnicosForm
    success_url = reverse_lazy('tecnicos_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Dados do tecnico atualizados com sucesso!')
        return response    
    
class TecnicosDelete(LoginRequiredMixin, DeleteView):
    model = models.Tecnicos
    template_name = 'tecnicos_delete.html'
    success_url = reverse_lazy('tecnicos_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Técnico excluído com sucesso!')
        return response
