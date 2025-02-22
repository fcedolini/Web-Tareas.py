from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo, CrearUsuario


# importar views q es donde se cra la vista de Http. se aplica metodo ".as_view()" porq en realidad es una lsita no una vista
urlpatterns = [
    path('', ListaPendientes.as_view(), name='pendientes'),
    path('registro/', CrearUsuario.as_view(), name='registro'),
    path('login/', Logueo.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
    path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
    path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea'),
]
