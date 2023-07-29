from django.db import models
# from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Vehiculo(models.Model):

    MARCA_CHOICES = [
        ('Fiat','Fiat'),
        ('Chevrolet','Chevrolet'),
        ('Ford','Ford'),
        ('Toyota','Toyota'),
    ]
    CATEGORIA_CHOICES = [
        ('particular','Particular'),
        ('transporte','Transporte'),
        ('carga','Carga'),
    ]
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=20,choices=MARCA_CHOICES,default='Ford',verbose_name='Marca')
    modelo = models.CharField(max_length=100,verbose_name='Modelo')
    carroceria = models.CharField(max_length=50,verbose_name='Serial Carrocería')
    motor = models.CharField(max_length=50,verbose_name='Serial Motor')
    categoria = models.CharField(max_length=20,choices=CATEGORIA_CHOICES,default='particular',verbose_name='Categoría')
    precio = models.IntegerField(verbose_name='Precio')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.modelo
    
    class Meta:
        permissions = (
            ("visualizar_catalogo","puede visualizar lista de vehiculos"),
            ("can_add_vehiculo","puede agregar vehiculo")
        )
        verbose_name = 'vehiculo'
        verbose_name_plural = 'vehiculos'
        ordering = ['created']

