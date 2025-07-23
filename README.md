
Proyecto de estilo blog sobre Libros y autores

# Guardo para saber como usar los comandos

1- Crear entorno virtual:
```
python -m venv env
 En Windows: env\Scripts\activate
```

2- Instalar Django:
```
pip install django
```

3- Migrar y entrar al server:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


# Funcionalidades
 Agregar autor: `/autor/`
 Agregar categoría: `/categoria/`
 Agregar post: `/post/`
 Buscar post: `/buscar/`
 Dejar mensaje: `/mensajes/` 
 ( Mensajes
Bandeja de entrada: /mensajes/
Enviar mensaje: /mensajes/enviar/
solo usuarios registrados pueden usar esta función)
Y por ultimo acerca de mí.

 # Usuarios
 Registro de usuario: /signup/
 Login: /login/
 Logout: /logout/
 Vista de perfil con: nombre, apellido, email, avatar, biografía, cumpleaños
 Edición de perfil: /profile/edit/
 Cambio de contraseña para el usuario si lo necesita

 # Video tutorial de mi pagina de blog
https://drive.google.com/file/d/1E1JcLvsk0_t9crhYHrv0N8LGoxbhZmPe/view?usp=sharing


Y por ultimo  un video explicativo, de como se usa mi blog de libros y se muestran las siguientes cosas:
- Navegación entre vistas (Home, About, Posts)
- Registro, login y perfil del usuario
- CRUD de páginas (crear, editar, borrar)
- Sistema de mensajería entre usuarios
