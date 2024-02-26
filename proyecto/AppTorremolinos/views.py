from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.utils import timezone

# Create your views here.

# Pagina Inicio/ Vista principal
class PaginaInicio(generic.ListView): 
    model = models.Deporte
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        ultimos_partidos_jugados = models.Partido.objects.filter(fecha_hora__lt=timezone.now()).order_by("-fecha_hora")[:5]
        proximos_partidos = models.Partido.objects.filter(fecha_hora__gte=timezone.now()).order_by("fecha_hora")[:5]

        context = super().get_context_data(**kwargs)
        context["ultimos_partidos_jugados"] = ultimos_partidos_jugados
        context["proximos_partidos"] = proximos_partidos
        return context


# Vistas modelo Deporte.

class DeporteListView(generic.ListView):
    model = models.Deporte
    template_name = 'listado_deportes.html'
    context_object_name = 'listado_deportes'

    def get_queryset(self):
        return models.Deporte.objects.all()
    
class DeporteCreateView(generic.CreateView):
    model = models.Deporte
    # form_class = DeporteForm
    template_name = 'crear_deporte.html'
    success_url = reverse_lazy('AppTorremolinos:listado_deportes.html') 

class DeporteDeleteView(generic.DeleteView):
    model = models.Deporte
    template_name = 'borrar_deporte.html'
    success_url = reverse_lazy('AppTorremolinos:listado_deportes.html') 

class DeporteUpdateView(generic.UpdateView):
    model = models.Deporte
    # form_class = DeporteForm
    template_name = 'actualizar_deporte.html'
    success_url = reverse_lazy('AppTorremolinos:listado_deportes.html') 


# Vistas modelo Instalacion.
class InstalacionesListView(generic.ListView):
    template_name = 'listado_instalaciones.html'
    context_object_name = 'listado_instalaciones'

    def get_queryset(self):
        return models.Instalacion.objects.all()

class InstalacionesCreateView(generic.CreateView):
    model = models.Instalacion
    # form_class = InstalacionForm
    template_name = 'instalaciones_create.html'
    # success_url = reverse_lazy('torre_crud:instalaciones-list')

class InstalacionesDeleteView(generic.DeleteView):
    model = models.Instalacion
    template_name = 'instalaciones_delete.html'
    # success_url = reverse_lazy('torre_crud:instalaciones-list')

class InstalacionesUpdateView(generic.UpdateView):
    model = models.Instalacion
    # form_class = InstalacionForm
    template_name = 'instalaciones_update.html'
    # success_url = reverse_lazy('torre_crud:instalaciones-list')


# Vistas del modelo Equipo.

class EquipoListView(generic.ListView):
    template_name = 'listado_equipos.html'
    context_object_name = 'listado_equipos'

    def get_queryset(self):
        return models.Equipo.objects.all()

class EquipoCreateView(generic.CreateView):
    model = models.Equipo
    # form_class = EquipoForm
    template_name = 'equipo_create.html'
    # success_url = reverse_lazy('torre_crud:equipos-list')

class EquipoDeleteView(generic.DeleteView):
    model = models.Equipo
    template_name = 'equipo_confirm_delete.html'
    # success_url = reverse_lazy('torre_crud:equipos-list')

class EquipoUpdateView(generic.UpdateView):
    model = models.Equipo
    # form_class = EquipoForm
    template_name = 'equipo_update.html'
    # success_url = reverse_lazy('torre_crud:equipos-list')

class EquipoDetailView(generic.DetailView):
    model = models.Equipo
    template_name = 'detalle_equipo.html'
    context_object_name = 'detalle_equipo'

    def get_queryset(self):
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        equipo = self.get_object()
        jugadores = models.Jugador.objects.filter(id_equipo=equipo)
        contexto['jugadores'] = jugadores
        return contexto
    

class EquipoJugadorCreate(generic.CreateView):
    model = models.Jugador
    # form_class = JugadorForm
    template_name = 'equipo_jugador_create.html'
    # success_url = reverse_lazy('torre_crud:equipos-list') 

    def get_initial(self):
        initial = super().get_initial()
        equipo_id = self.kwargs.get('pk')
        equipo = models.Equipo.objects.get(pk=equipo_id)
        initial['equipo'] = equipo
        return initial


# Vistas del modelo Jugador.
class JugadorListView(generic.ListView):
    model = models.Jugador
    template_name = 'listado_jugadores.html'
    context_object_name = 'jugadores'
    

class JugadorCreateView(generic.CreateView):
    model = models.Jugador
    # form_class = JugadorForm
    # success_url = reverse_lazy('torre_crud:jugadores-list') 
    template_name = 'jugador_create.html'

class JugadorUpdateView(generic.UpdateView):
    model = models.Jugador
    # form_class = JugadorForm
    # success_url = reverse_lazy('torre_crud:jugadores-list') 
    template_name = 'jugador_update.html'

class JugadorDetailView(generic.DetailView):
    model = models.Jugador
    template_name = 'detalle_jugador.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jugador = self.get_object()
        context['equipo'] = jugador.id_equipo.nombre
        context['elJugador'] = jugador
        return context

class JugadorDeleteView(generic.DeleteView):
    model = models.Jugador
    # success_url = reverse_lazy('torre_crud:jugadores-list')  
    template_name = 'jugador_confirm_delete.html'


# Vistas del modelo Partido.
class PartidoListView(generic.ListView):
    model = models.Partido
    template_name = 'partido_list.html'
    context_object_name = 'partidos'
    ordering = ['-fecha_hora']

class PartidoCreateView(generic.CreateView):
    model = models.Partido
    # form_class = PartidoForm
    # success_url = reverse_lazy('torre_crud:partidos-list') 
    template_name = 'partido_create.html'

class PartidoUpdateView(generic.UpdateView):
    model = models.Partido
    # form_class = PartidoForm
    # success_url = reverse_lazy('torre_crud:partidos-list') 
    template_name = 'partido_update.html'

class PartidoDetailView(generic.DetailView):
    model = models.Partido
    template_name = 'partido_detail.html'
    context_object_name = 'partido'

class PartidoDeleteView(generic.DeleteView):
    model = models.Partido
    # success_url = reverse_lazy('torre_crud:partidos-list')
    template_name = 'partido_confirm_delete.html'