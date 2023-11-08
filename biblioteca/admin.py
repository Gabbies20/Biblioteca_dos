from django.contrib import admin
from .models import Biblioteca,Escritor,Book,Lector,DatosLector



# Register your models here.
admin.site.register(Biblioteca)
admin.site.register(Escritor)
admin.site.register(Book)
admin.site.register(Lector)
admin.site.register(DatosLector)