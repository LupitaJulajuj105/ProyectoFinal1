from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista, name='becas_list'),
    path('nuevo/', views.crear, name='becas_create'),
    path('editar/<int:id>/', views.editar, name='becas_edit'),
    path("becas/", views.becas_list, name="becas_list"),
    path("becas/<int:id>/", views.becas_detail, name="becas_detail"),
]
