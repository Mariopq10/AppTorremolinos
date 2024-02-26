from django.urls import path
from . import views

app_name = 'AppTorremolinos'

urlpatterns = [
    path('', views.PaginaInicio.as_view(), name='PaginaInicio'),

    # URL para deportes
    path('deportes/', views.DeporteListView.as_view(), name='listado_deportes'),
    path('deportes/crear/', views.DeporteCreateView.as_view(), name='crear_deporte'),
    path('deportes/<int:pk>/actualizar/', views.DeporteUpdateView.as_view(), name='actualizar_deporte'),
    path('deportes/<int:pk>/eliminar/', views.DeporteDeleteView.as_view(), name='borrar_deporte'),

    # URLs para Instalaciones
    path('instalaciones/', views.InstalacionesListView.as_view(), name='listado_instalaciones'),
    path('instalaciones/crear/', views.InstalacionesCreateView.as_view(), name='crear_instalaciones'),
    path('instalaciones/<int:pk>/actualizar/', views.InstalacionesUpdateView.as_view(), name='actualizar_instalaciones'),
    path('instalaciones/<int:pk>/eliminar/', views.InstalacionesDeleteView.as_view(), name='borrar_instalaciones'),

    # URLs para Equipos
    path('equipos/', views.EquipoListView.as_view(), name='listado_equipos'),
    path('equipos/crear/', views.EquipoCreateView.as_view(), name='crear_equipo'),
    path('equipos/<int:pk>/actualizar/', views.EquipoUpdateView.as_view(), name='actualizar_equipo'),
    path('equipos/<int:pk>/eliminar/', views.EquipoDeleteView.as_view(), name='borrar_equipo'),
    path('equipos/<int:pk>/', views.EquipoDetailView.as_view(), name='detalle_equipo'),
    path('equipos/<int:pk>/jugadores', views.EquipoJugadorCreate.as_view(), name='crear_jugador_equipo'),

    # URLs para Jugadores
    path('jugadores/', views.JugadorListView.as_view(), name='listado_jugadores'),
    path('jugadores/crear/', views.JugadorCreateView.as_view(), name='crear_jugador'),
    path('jugadores/<int:pk>/editar/', views.JugadorUpdateView.as_view(), name='actualizar_jugador'),
    path('jugadores/<int:pk>/eliminar/', views.JugadorDeleteView.as_view(), name='borrar_jugador'),
    path('jugadores/<int:pk>/', views.JugadorDetailView.as_view(), name='detalle_jugador'),

    # URLs para Partidos
    path('partidos/', views.PartidoListView.as_view(), name='listado_partidos'),
    path('partidos/crear/', views.PartidoCreateView.as_view(), name='crear_partido'),
    path('partidos/<int:pk>/editar/', views.PartidoUpdateView.as_view(), name='actualizar_partido'),
    path('partidos/<int:pk>/eliminar/', views.PartidoDeleteView.as_view(), name='borrar_partido'),
    path('partidos/<int:pk>/', views.PartidoDetailView.as_view(), name='detalle_partido'),
   
]
