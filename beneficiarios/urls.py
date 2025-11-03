from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista, name='beneficiarios_list'),
    path('nuevo/', views.crear, name='beneficiarios_create'),
    path('editar/<int:id>/', views.editar, name='beneficiarios_edit'),
    path('detalle/<int:id>/', views.detalle, name='beneficiarios_detail'),
    path('beneficiarios/<int:id>/eliminar/', views.eliminar_beneficiario, name='eliminar_beneficiario'),
    path('beneficiarios/eliminar/buscar/', views.buscar_eliminar_beneficiario, name='buscar_eliminar_beneficiario'),
    path("beneficiarios/detalleBene/", views.detalles_bene, name="beneficiarios_detalleBene"),

]



