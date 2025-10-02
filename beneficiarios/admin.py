from django.contrib import admin
from .models import *
# Register models in admin if needed
from .models import HistorialUsuarios

admin.site.register(HistorialUsuarios)