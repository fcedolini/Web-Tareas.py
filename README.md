Proyecto web de tareas pendientes<br>

https://lista-pendientes-8a3822cd752a.herokuapp.com/login/

-Web que permite crear, editar y eliminar una lista de tareas para cada usuario registrado<br>
Tec en uso: Python, Django 5.1 y sqlite

Usuario de prueba <br>
user: pedro<br>
pass: Limbo202020

Funcionalidades:<br>
-Logueo y deslogueo de usuarios. LoginView<br>
-Restringir acceso a las Urls a usuarios sin logueo. LoginRequiredMixin<br>
-Filtro para recibir la info solo del user logueado y no del resto. Reescribiendo method get_context_data()<br>
-Asigna las tareas creada directo al user logueado en vez de consultar autor. Vista CrarTarea reescribiendo el method form_valid()<br>
-Barra de búsqueda aplicando filtros en la vista, por usuario y por Título de tarea

