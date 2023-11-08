from django.db import models

from django.utils import timezone

# Create your models here.
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    
    def __str__(self) -> str:
        return self.nombre
    
    
class Escritor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200,blank=True)
    #Null indica si queremos que se guarde como nulo el valor si no se introduce nada. Por defecto: False.
    edad = models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return self.nombre
    

class Book(models.Model):
    IDIOMAS = [
        ("ES", "Español"),
        ("EN", "Inglés"),
        ("FR", "Francés"),
        ("IT", "Italiano"),
    ]

    nombre = models.CharField(max_length=200)
    tipo = models.CharField(
        max_length=2,
        choices=IDIOMAS,
        default="ES",
    )
    
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    escritor = models.ManyToManyField(Escritor)
    
    def __str__(self) -> str:
        return self.nombre
    
class Lector(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=200,unique=True)
    #db_column: indica el nombre de la columna en la base de datos, por defecto el del atributo.
    puntos = models.FloatField(default=5.0,db_column='puntos biblioteca')
    #Relacion ManytoMany con el parametro throught, en el indico esta relacion con la tabla intermedia Préstamo.
    libros_prestamos = models.ManyToManyField(Book, 
                                    through='Prestamo',
                                    #Cuando queremos añadir varias relaciones desde un modelo hacia el mismo modelo, debemos incluir el parametro related_name.
                                    related_name="l_prestamo")
    libros_preferidos = models.ForeignKey(Book,
                                          on_delete = models.CASCADE,
                                          related_name="l_preferidos")
    
    def __str__(self) -> str:
        return self.nombre
    
class DatosLector(models.Model):
    direccion = models.TextField()
    gustos = models.TextField()
    telefono = models.IntegerField()
    lector = models.OneToOneField(Lector,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.lector
    
    
class Prestamo(models.Model):
    cliente = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Book, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.fecha_prestamo
    
    