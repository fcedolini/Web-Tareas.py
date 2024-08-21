from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# importar el modelo o DB creado en models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Tarea


# para conectarse
class Logueo(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('pendientes')


# Se cra la vista http q retorna la web y luego se la incluye en urls.py de este mismo nivel
# crear clase para mostrar lista con "ListView"
class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    # agregar un nombre de context para en vez de llamdar a object_list llamemos a 'tareas'
    context_object_name = 'tareas'

    # Sobreescribir el metodo para obtener los datos solo del usuario conectado
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tareas"] = context["tareas"].filter(
            usuario=self.request.user)
        context["count"] = context["tareas"].filter(completo=False).count()
        # Buscar y filtrar tareas
        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context["tareas"] = context["tareas"].filter(
                titulo__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context


# Crear vista para el detalle de las tareas, para cuando le damos click
class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    # cambiar nombre del archivo busccado por el url
    template_name = 'base/tarea_det.html'


class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('pendientes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)


class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('pendientes')


class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('pendientes')


class CrearUsuario(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('pendientes')

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(CrearUsuario, self).form_valid(form)

    def get(self, *args: str, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('pendientes')
        return super(CrearUsuario, self).get(*args, **kwargs)
