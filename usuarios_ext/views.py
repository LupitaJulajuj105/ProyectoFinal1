from django.shortcuts import render, redirect
from django.db import connection

def _fetchone(query, params=()):
    with connection.cursor() as c:
        c.execute(query, params)
        return c.fetchone()

def _execute(query, params=()):
    with connection.cursor() as c:
        c.execute(query, params)
        return c.rowcount

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        row = _fetchone('SELECT id_usuario, username, password, rol FROM usuarios WHERE username=%s', (username,))
        if row and row[2] == password:
            request.session['user_id'] = row[0]
            request.session['username'] = row[1]
            request.session['user_rol'] = row[3]
            return redirect('/after_login/')
        else:
            error = 'Usuario o contraseña incorrectos.'
    return render(request, 'login.html', {'error': error})

def register_view(request):
    error = None
    success = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        existing = _fetchone('SELECT id_usuario FROM usuarios WHERE username=%s', (username,))
        if existing:
            error = 'El usuario ya existe.'
        else:
            _execute('INSERT INTO usuarios (username,password,rol,estado) VALUES (%s,%s,%s,%s)', (username,password,'estudiante','activo'))
            success = 'Cuenta creada. Ya puedes ingresar.'
    return render(request, 'register.html', {'error': error, 'success': success})

def logout_view(request):
    request.session.flush()
    return redirect('/')

def after_login(request):
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
