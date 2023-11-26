from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Evento, TipoUsuario, Segmento

class EventoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "fechaInicio", "fechaTermino")

class TipoUsuarioAdmin(UserAdmin):
    model = TipoUsuario
    list_display = ('username', 'email', 'first_name', 'last_name', 'tipo_cuenta')
    fieldsets = UserAdmin.fieldsets + (
        ('Segmento', {'fields': ('tipo_cuenta',)}),
    )

admin.site.register(TipoUsuario, TipoUsuarioAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Segmento)
