from django.shortcuts import render
from .models import Book,Prestamo,Lector
from django.db.models import Q,F,Avg,Max,Min


def index(request):
    # Lógica de la vista
    return render(request, 'biblioteca/index.html')


#Vista que muestre todos los libros:
def listar_libros(request):
    libros = Book.objects.select_related('biblioteca').prefetch_related('escritor')
    return render(request,'biblioteca/listar_libros.html',{'mostrar_libros':libros})


#Vista para acceder a un libro en concreto:
def libro_en_concreto(request,id_libro):
    libro =Book.objects.select_related('biblioteca').prefetch_related('escritor').get(id=id_libro)
    print("Valor de libro.id:", libro.id)
    return render(request,'biblioteca/libro_concreto.html',{'libro_mostrar':libro})
    
#vista  que muestre los libros de un año y mes concreto:
def anio_concreto(request,id_anio,id_mes):
    libro = Book.objects.select_related('biblioteca').prefetch_related('escritor').filter(fecha_publicacion__year=id_anio,fecha_publicacion__month=id_mes).all()
    return render 

#Vista que obtenga los libros que tienen el idioma del libro o español ordenados por fecha de publicación.
def idioma_libro(request,idioma):
    libros = Book.objects.select_related('biblioteca').prefetch_related('escritor')
    #La letra Q con | sirven para poder hacer filtros con OR
    libros = libros.filter(Q(tipo=idioma)| Q(tipo='ES')).order_by('fecha_publicacion')
    return render (request,'biblioteca/lista.html',{'libros_mostrar':libros})

#o

    """def libros_biblioteca(request, id_biblioteca, texto):
    libros = Book.objects.select_related('biblioteca').prefetch_related('escritor')
    libros = libros.filter(biblioteca=id_biblioteca, descripcion__contains=texto).order_by('-nombre')
    
    # Crear una nueva variable en la vista
    idioma = libros.first().get_tipo_display if libros.exists() else "Desconocido"
    
    return render(request, 'biblioteca/libros_biblioteca.html', {'libros_mostrar': libros, 'idioma': idioma})

    """

#Vista que obtenga los libros de una biblioteca que contenga un texto en concreto:
def libros_biblioteca(request,id_biblioteca,texto):
    libros = Book.objects.select_related('biblioteca').prefetch_related('escritor')
    libros = libros.filter(biblioteca=id_biblioteca,descripcion__contains=texto).order_by('-nombre')
    return render(request,'biblioteca/libros_biblioteca.html',{'libros_mostrar':libros})

#Vista que obtenga el ultimo cliente que se llevo un libro en concreto:
def cliente_ultimo_libro(request,id_libro):
    cliente = Prestamo.objects
    pass

#
def dame_libros_titulo_en_descripcion(request):
    libros = Book.objects.select_related('biblioteca').prefetch_related('escritor')
    libros = libros.filter(descripcion__contains=F("nombre"))
    return render(request,'biblioteca/descripcion.html',{'libros_mostrar':libros})

    """
    
    La expresión F() en Django es una forma de referenciar un campo de un modelo dentro de una consulta. Se utiliza para comparar un campo con el valor de otro campo en el mismo modelo. Esto es especialmente útil cuando deseas realizar comparaciones entre campos de la misma instancia de un modelo en una consulta de base de datos.

Aquí tienes un ejemplo para entender cómo funciona F():

Supongamos que tienes un modelo Libro con dos campos: cantidad_disponible y cantidad_vendida. Si deseas actualizar la cantidad disponible restando la cantidad vendida, puedes hacerlo de la siguiente manera:

from django.db.models import F

libro = Libro.objects.get(id=1)
libro.cantidad_disponible = F('cantidad_disponible') - F('cantidad_vendida')
libro.save()


    
    """

#Vista eu obtiene la media, maximo y minimo de puntos de todos los clientes de la Biblioteca:


def dame_agrupaciones_puntos_cliente(request):
    clientes = Lector.objects.all()  # Obtener la lista de todos los clientes
    resultado = clientes.aggregate(media=Avg('puntos'), maximo=Max('puntos'), minimo=Min('puntos'))
    media = resultado['media']
    maximo = resultado['maximo']
    minimo = resultado['minimo']
    
    return render(request, 'biblioteca/agrupaciones.html', {'media': media, 'maximo': maximo, 'minimo': minimo, 'clientes': clientes})

    """
    aggregate:

aggregate se utiliza para realizar cálculos de agregación en todos los objetos de un queryset. Devuelve un diccionario de resultados de agregación.
Los cálculos se realizan en el conjunto de resultados completo y no generan una nueva columna en cada objeto del queryset.
Se utiliza para calcular valores globales, como el promedio, el máximo o el mínimo de un campo en todos los objetos.
Los resultados de aggregate son accesibles a través de claves en el diccionario devuelto.
from django.db.models import Avg
from myapp.models import Lector

resultado = Lector.objects.aggregate(media_puntos=Avg('puntos'))
media = resultado['media_puntos']



annotate:
annotate se utiliza para agregar información a cada objeto en el queryset sin realizar cálculos en el conjunto completo.
Puedes agregar valores calculados como nuevas columnas a cada objeto en el queryset.
Se utiliza cuando deseas enriquecer los objetos individuales con información adicional.
Los resultados de annotate son accesibles directamente como atributos en cada objeto del queryset.
from django.db.models import F
from myapp.models import Lector

clientes = Lector.objects.annotate(
    puntos_dobles=F('puntos') * 2
)
# Ahora cada objeto en 'clientes' tiene un atributo 'puntos_dobles'.


    """