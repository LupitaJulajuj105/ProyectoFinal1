from django.shortcuts import render, redirect
from django.db import connection
from datetime import datetime
from .models import Historial  # Asegúrate de tener este modelo creado y registrado en settings.py


# --- FUNCIONES AUXILIARES PARA CONSULTAS SQL ---
def _fetchone(query, params=()):
    """Ejecuta una consulta SELECT y devuelve una sola fila."""
    with connection.cursor() as c:
        c.execute(query, params)
        return c.fetchone()

def _execute(query, params=()):
    """Ejecuta una consulta INSERT, UPDATE o DELETE."""
    with connection.cursor() as c:
        c.execute(query, params)
        return c.rowcount


# --- LOGIN ---
def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificar si el usuario existe
        row = _fetchone(
            'SELECT id_usuario, username, password, rol FROM usuarios WHERE username=%s',
            (username,)
        )

        # Validar contraseña
        if row and row[2] == password:
            # Guardar datos en la sesión
            request.session['user_id'] = row[0]
            request.session['username'] = row[1]
            request.session['user_rol'] = row[3]

            # Registrar el inicio de sesión en la tabla historial
            Historial.objects.create(
                id_usuario=row[0],
                accion='Inicia Sesión',
                tabla='usuarios',
                fecha_hora=datetime.now()
            )

            return redirect('/after_login/')
        else:
            error = 'Usuario o contraseña incorrectos.'

    return render(request, 'login.html', {'error': error})


# --- REGISTRO DE USUARIO ---
def register_view(request):
    error = None
    success = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificar si ya existe el usuario
        existing = _fetchone('SELECT id_usuario FROM usuarios WHERE username=%s', (username,))
        if existing:
            error = 'El usuario ya existe.'
        else:
            # Registrar nuevo usuario
            _execute(
                'INSERT INTO usuarios (username, password, rol, estado) VALUES (%s, %s, %s, %s)',
                (username, password, 'estudiante', 'activo')
            )
            success = 'Cuenta creada correctamente. Ya puedes iniciar sesión.'

    return render(request, 'register.html', {'error': error, 'success': success})


# --- LOGOUT ---
def logout_view(request):
    """Cierra la sesión y registra el evento en historial."""
    user_id = request.session.get('user_id')

    if user_id:
        # Registrar cierre de sesión
        Historial.objects.create(
            id_usuario=user_id,
            accion='Cierra Sesión',
            tabla='usuarios',
            fecha_hora=datetime.now()
        )

    # Limpiar la sesión
    request.session.flush()
    return redirect('/')


# --- REDIRECCIÓN SEGÚN ROL ---
def after_login(request):
    """Redirige al dashboard correspondiente según el rol del usuario."""
    rol = request.session.get('user_rol')

    if rol == 'administrador':
        request.session['user_rol_css'] = '/static/css/roles/admin.css'
        return redirect('/dashboard/admin/')
    elif rol == 'comitiva':
        request.session['user_rol_css'] = '/static/css/roles/comitiva.css'
        return redirect('/dashboard/comitiva/')
    else:
        request.session['user_rol_css'] = '/static/css/roles/estudiante.css'
        return redirect('/dashboard/estudiante/')
