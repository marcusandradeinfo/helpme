from django.contrib import admin
from . import models

class ChamadosAdmin(admin.ModelAdmin):
    list_display = ('numero_chamado',)
    search_fields = ('numero_chamado',)

class StatusChamadosAdmin(admin.ModelAdmin):
    list_display = ('status',)
    search_fields = ('status',)

admin.site.register(models.Chamados, ChamadosAdmin)
admin.site.register(models.StatusChamados, StatusChamadosAdmin)
