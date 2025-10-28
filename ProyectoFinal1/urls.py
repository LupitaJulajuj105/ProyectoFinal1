from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns = [
    path('dashboard/admin/', lambda r: __import__('django.shortcuts', fromlist=['']).render(r, 'dashboard_admin.html')),
    path('dashboard/estudiante/', lambda r: __import__('django.shortcuts', fromlist=['']).render(r, 'dashboard_estudiante.html')),
    path('dashboard/comitiva/', lambda r: __import__('django.shortcuts', fromlist=['']).render(r, 'dashboard_comitiva.html')),

    path('', include('usuarios_ext.urls')),

    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('beneficiarios/', include('beneficiarios.urls')),
    path('becas/', include('becas.urls')),
    path('solicitudes/', include('solicitudes.urls')),
    path('consultas/', include('consultas.urls')),
]
