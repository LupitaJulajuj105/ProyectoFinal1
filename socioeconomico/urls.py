from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='socioeconomico_list'),
    path('crear/', views.crear, name='socioeconomico_create'),
    path('editar/<int:id>/', views.editar, name='socioeconomico_edit'),
    path('detalle/<int:id>/', views.detalle, name='socioeconomico_detail'),
    path('eliminar/<int:id>/', views.eliminar, name='socioeconomico_delete'),
    path('detalles_socioeconomico/', views.detalles_socioeconomico, name='detalles_socioeconomico'),
]
