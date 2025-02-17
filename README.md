Proyecto web de tareas pendientes

-Web que permite crear, editar y eliminar una lista de tareas para cada usuario registrado
Tec en uso: Django 5.1 y sqlite

Usuario de prueba
user: pedro
pass: Limbo202020

Funcionalidades:
-Logueo y deslogueo de usuarios. LoginView
-Restringir acceso a las Urls a usuarios sin logueo. LoginRequiredMixin
-Recibir la info solo del user logueado y no del resto. Reescribiendo method get_context_data()
-Asigna las tareas creada directo al user logueado en vez de consultar autor. Vista CrarTarea reescribiendo el method form_valid()
-Barra de búsqueda aplicando filtros en la vista, por usuario y por Título de tarea
