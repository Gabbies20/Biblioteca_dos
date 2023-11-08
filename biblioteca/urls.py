from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar_libros',views.listar_libros,name='listar_libros'),
    path("libro_en_concreto/<int:id_libro>/",views.libro_en_concreto,name='libro_en_concreto'),
    path('idioma/<str:idioma>',views.idioma_libro,name='idioma'),
    path('libros_biblioteca/<int:id_biblioteca>/libros/<str:texto>',views.libros_biblioteca,name='libros_biblioteca'),
    path('dame_libros_titulo_descripcion',views.dame_libros_titulo_en_descripcion,name='dame_libros_titulo_en_descripcion'),
    path('agrupaciones',views.dame_agrupaciones_puntos_cliente,name='agrupaciones')
]