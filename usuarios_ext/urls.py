from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('after_login/', views.after_login, name='after_login'),
    path('logout/', views.logout_view, name='logout'),
    path('historial-usuarios/', views.consulta_historial_usuarios, name='consulta_historial_usuarios'),
   path('contactos/', TemplateView.as_view(template_name='contactos.html'), name='contactos'),
]
