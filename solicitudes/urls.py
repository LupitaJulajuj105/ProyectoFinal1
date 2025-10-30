from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista, name='solicitudes_list'),
    path('nuevo/', views.crear, name='solicitudes_create'),
    path('editar/<int:id>/', views.editar, name='solicitudes_edit'),
   path("solicitudes/", views.solicitudes_list, name="solicitudes_list"),
   path("solicitudes/<int:id>/", views.solicitudes_detail, name="solicitudes_detail"), 
   path("detalles_soli/", views.detalles_soli, name="detalles_soli"),
]
