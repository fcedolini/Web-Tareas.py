from django.db import models
from django.contrib.auth.models import User


# Crear mediante clase la estructura de la base de datos, luego registrarla y hacer migraciones
class Tarea(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    # nombre con el q se ve la tarea cargada
    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['completo']

# luego de crear la estructura se debe migrar: python manage.py makemigrations
# python manage.py migrate para hacer las migras y aplicar cambios y crear BD
