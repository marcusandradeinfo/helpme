from django.contrib import admin
from . import models

class NivelAdmin(admin.ModelAdmin):
    list_display = ('nivel',)
    search_fields = ('nivel',)

class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


class BairroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class StatusClienteAdmin(admin.ModelAdmin):
    list_display = ('status',)
    search_fields = ('status',)


admin.site.register(models.Clientes, ClientesAdmin)
admin.site.register(models.Cidade, CidadeAdmin)
admin.site.register(models.Estado, EstadoAdmin)
admin.site.register(models.Bairro, BairroAdmin)
admin.site.register(models.Nivel, NivelAdmin)
admin.site.register(models.StatusClientes, StatusClienteAdmin)