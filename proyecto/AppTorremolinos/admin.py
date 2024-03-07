from django.contrib import admin
from . import models

# Register your models here.
class DeporteAdmin(admin.ModelAdmin):
    list_display = ["id_deporte", "nombre"]
    search_fields = ["nombre"]
    list_filter = ["nombre"]

admin.site.register(models.Deporte, DeporteAdmin)

class InstalacionAdmin(admin.ModelAdmin):
    list_display = ["id_instalacion", "nombre", "direccion", "iluminacion", "cubierta"]
    search_fields = ["nombre"]
    list_filter = ["nombre"]

admin.site.register(models.Instalacion, InstalacionAdmin)

class EquipoAdmin(admin.ModelAdmin):
    list_display = ["id_equipo", "nombre", "id_deporte", "equipacion_principal",
        "equipacion_suplente", "contacto", "telefono", "email",
    ]
    search_fields = ["nombre", "id_deporte", "contacto"]
    list_filter = ["nombre", "id_deporte", "contacto"]

admin.site.register(models.Equipo, EquipoAdmin) 

class JugadorAdmin(admin.ModelAdmin):
    list_display=["nombre", "apellido1", "apellido2", "id_equipo"]
    search_fields=["nombre", "apellido1", "apellido2", "id_equipo"]
    list_filter=["nombre", "apellido1", "apellido2", "id_equipo"]

admin.site.register(models.Jugador, JugadorAdmin)

class PartidoAdmin(admin.ModelAdmin):
    list_display = ["id_partido", "id_deporte", "fecha_hora", "id_instalacion",
        "id_local", "id_visitante", "puntos_local", "puntos_visitante", "observaciones",
    ]
    search_fields = ["id_deporte", "id_instalacion", "id_local", "id_visitante"]
    list_filter = ["id_deporte", "id_instalacion", "id_local", "id_visitante"]

admin.site.register(models.Partido, PartidoAdmin)