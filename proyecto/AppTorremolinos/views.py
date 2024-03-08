from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import DeporteForm, EquipoForm, InstalacionForm, JugadorForm, PartidoForm
from . import models
from django.views import generic
from django.utils import timezone

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


# Vistas modelo Deporte

class DeporteListView(generic.ListView):
    model = models.Deporte
    template_name = 'listado_deportes.html'
    context_object_name = 'listado_deportes'

    def get_queryset(self):
        return models.Deporte.objects.all()
    
class DeporteCreateView(generic.CreateView):
    model = models.Deporte
    form_class = DeporteForm
    template_name = 'crear_deporte.html'
    success_url = reverse_lazy('AppTorremolinos:listado_deportes') 

class DeporteDeleteView(generic.DeleteView):
    model = models.Deporte
    template_name = 'borrar_deporte.html'
    success_url = reverse_lazy('AppTorremolinos:listado_deportes') 

class DeporteUpdateView(generic.UpdateView):
    model = models.Deporte
    form_class = DeporteForm
    template_name = 'actualizar_deporte.html'
    success_url = reverse_lazy('AppTorremolinos:listado_deportes') 


# Vistas modelo Instalacion
    
class InstalacionesListView(generic.ListView):
    template_name = 'listado_instalaciones.html'
    context_object_name = 'listado_instalaciones'

    def get_queryset(self):
        return models.Instalacion.objects.all()

class InstalacionesCreateView(generic.CreateView):
    model = models.Instalacion
    form_class = InstalacionForm
    template_name = 'crear_instalaciones.html'
    success_url = reverse_lazy('AppTorremolinos:listado_instalaciones')

class InstalacionesDeleteView(generic.DeleteView):
    model = models.Instalacion
    template_name = 'borrar_instalaciones.html'
    success_url = reverse_lazy('AppTorremolinos:listado_instalaciones')
class InstalacionesUpdateView(generic.UpdateView):
    model = models.Instalacion
    form_class = InstalacionForm
    template_name = 'actualizar_instalaciones.html'
    success_url = reverse_lazy('AppTorremolinos:listado_instalaciones')


# Vistas del modelo Equipo

class EquipoListView(generic.ListView):
    template_name = 'listado_equipos.html'
    context_object_name = 'listado_equipos'

    def get_queryset(self):
        return models.Equipo.objects.all()

class EquipoCreateView(generic.CreateView):
    model = models.Equipo
    form_class = EquipoForm
    template_name = 'crear_equipo.html'
    success_url = reverse_lazy('AppTorremolinos:listado_equipos')

class EquipoDeleteView(generic.DeleteView):
    model = models.Equipo
    template_name = 'borrar_equipo.html'
    success_url = reverse_lazy('AppTorremolinos:listado_equipos')

class EquipoUpdateView(generic.UpdateView):
    model = models.Equipo
    form_class = EquipoForm
    template_name = 'actualizar_equipo.html'
    success_url = reverse_lazy('AppTorremolinos:listado_equipos')

class EquipoDetailView(generic.DetailView):
    model = models.Equipo
    template_name = 'detalle_equipo.html'
    context_object_name = 'equipo'

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
    form_class = JugadorForm
    template_name = 'crear_jugador_equipo.html'
    success_url = reverse_lazy('AppTorremolinos:listado_equipos') 

    def get_initial(self):
        initial = super().get_initial()
        equipo_id = self.kwargs.get('pk')
        equipo = models.Equipo.objects.get(pk=equipo_id)
        initial['equipo'] = equipo
        return initial


# Vistas del modelo Jugador
    
class JugadorListView(generic.ListView):
    model = models.Jugador
    template_name = 'listado_jugadores.html'
    context_object_name = 'jugadores'
    

class JugadorCreateView(generic.CreateView):
    model = models.Jugador
    form_class = JugadorForm
    success_url = reverse_lazy('AppTorremolinos:listado_jugadores') 
    template_name = 'crear_jugador.html'
    

class JugadorUpdateView(generic.UpdateView):
    model = models.Jugador
    form_class = JugadorForm
    success_url = reverse_lazy('AppTorremolinos:listado_jugadores')  
    template_name = 'actualizar_jugador.html'

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
    success_url = reverse_lazy('AppTorremolinos:listado_jugadores')  
    template_name = 'borrar_jugador.html'


# Vistas del modelo Partido
    
class PartidoListView(generic.ListView):
    model = models.Partido
    template_name = 'listado_partidos.html'
    context_object_name = 'partidos'
    ordering = ['-fecha_hora']

class PartidoCreateView(generic.CreateView):
    model = models.Partido
    form_class = PartidoForm
    success_url = reverse_lazy('AppTorremolinos:listado_partidos') 
    template_name = 'crear_partido.html'

class PartidoUpdateView(generic.UpdateView):
    model = models.Partido
    form_class = PartidoForm
    success_url = reverse_lazy('AppTorremolinos:listado_partidos') 
    template_name = 'actualizar_partido.html'

class PartidoDetailView(generic.DetailView):
    model = models.Partido
    template_name = 'detalle_partido.html'
    context_object_name = 'partido'

class PartidoDeleteView(generic.DeleteView):
    model = models.Partido
    success_url = reverse_lazy('AppTorremolinos:listado_partidos') 
    template_name = 'borrar_partido.html'