from django.contrib import admin
from . import models

class FormacaoTecnicoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


class TecnicosAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


admin.site.register(models.FormacaoTecnico, FormacaoTecnicoAdmin)
admin.site.register(models.Tecnicos, TecnicosAdmin)
