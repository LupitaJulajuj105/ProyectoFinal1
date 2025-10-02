ProyectoFinal1 - Sistema de Becas (scaffold)

Instrucciones rápidas:
1. Instala dependencias:
   pip install django mysqlclient

2. Ajusta las credenciales de la DB en ProyectoFinal1/settings.py si es necesario.

3. Opcional: si tu base de datos ya tiene las tablas (importaste el SQL), NO ejecutes migrate para evitar conflictos.
   Si deseas usar los modelos Django desde cero, ejecuta:
      python manage.py makemigrations
      python manage.py migrate

4. Ejecuta el servidor:
      python manage.py runserver

Las apps incluidas: beneficiarios, becas, solicitudes, consultas (varias páginas de consulta).
