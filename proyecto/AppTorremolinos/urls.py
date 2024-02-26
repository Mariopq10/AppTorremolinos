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
    path('instalaciones/crear/', views.InstalacionesCreateView.as_view(), name='instalaciones-create'),
    path('instalaciones/<int:pk>/actualizar/', views.InstalacionesUpdateView.as_view(), name='instalaciones-update'),
    path('instalaciones/<int:pk>/eliminar/', views.InstalacionesDeleteView.as_view(), name='instalaciones-delete'),

    # URLs para Equipos
    path('equipos/', views.EquipoListView.as_view(), name='listado_equipos'),
    path('equipos/crear/', views.EquipoCreateView.as_view(), name='equipos-create'),
    path('equipos/<int:pk>/actualizar/', views.EquipoUpdateView.as_view(), name='equipos-update'),
    path('equipos/<int:pk>/eliminar/', views.EquipoDeleteView.as_view(), name='equipos-delete'),
    path('equipos/<int:pk>/', views.EquipoDetailView.as_view(), name='detalle_equipo'),
    path('equipos/<int:pk>/jugadores', views.EquipoJugadorCreate.as_view(), name='equipo-jugador-create'),

    # URLs para Jugadores
    path('jugadores/', views.JugadorListView.as_view(), name='listado_jugadores'),
    path('jugadores/crear/', views.JugadorCreateView.as_view(), name='jugadores-create'),
    path('jugadores/<int:pk>/editar/', views.JugadorUpdateView.as_view(), name='jugadores-update'),
    path('jugadores/<int:pk>/eliminar/', views.JugadorDeleteView.as_view(), name='jugadores-delete'),
    path('jugadores/<int:pk>/', views.JugadorDetailView.as_view(), name='detalle_jugador'),

    # URLs para Partidos
    path('partidos/', views.PartidoListView.as_view(), name='listado_partidos'),
    path('partidos/crear/', views.PartidoCreateView.as_view(), name='partidos-create'),
    path('partidos/<int:pk>/editar/', views.PartidoUpdateView.as_view(), name='partidos-update'),
    path('partidos/<int:pk>/eliminar/', views.PartidoDeleteView.as_view(), name='partidos-delete'),
    path('partidos/<int:pk>/', views.PartidoDetailView.as_view(), name='detalle_partido'),
   
]
