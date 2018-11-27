from django.contrib import admin
from .models import Empresa, Colaborador, Insumo, Turno


admin.site.register(Empresa)
admin.site.register(Colaborador)
admin.site.register(Insumo)
admin.site.register(Turno)