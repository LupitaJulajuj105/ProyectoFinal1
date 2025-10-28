from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_users(sender, **kwargs):
    try:
        from django.db import connection
        with connection.cursor() as c:
            # check table usuarios exists
            c.execute("SHOW TABLES LIKE 'usuarios';")
            if c.fetchone():
                # create if not exists
                c.execute("SELECT id_usuario FROM usuarios WHERE username='admin';")
                if not c.fetchone():
                    c.execute("INSERT INTO usuarios (username,password,rol,estado) VALUES ('admin','admin123','administrador','activo');")
                c.execute("SELECT id_usuario FROM usuarios WHERE username='comitiva';")
                if not c.fetchone():
                    c.execute("INSERT INTO usuarios (username,password,rol,estado) VALUES ('comitiva','comitiva123','comitiva','activo');")
                c.execute("SELECT id_usuario FROM usuarios WHERE username='estudiante';")
                if not c.fetchone():
                    c.execute("INSERT INTO usuarios (username,password,rol,estado) VALUES ('estudiante','estudiante123','estudiante','activo');")
    except Exception:
        pass

def ready():
    post_migrate.connect(create_users)
