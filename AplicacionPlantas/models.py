from django.db import models

class Usuario(models.Model):
    id_usuario= models.AutoField(primary_key= True)
    nombre= models.CharField(max_length= 40)
    correo= models.EmailField(max_length= 100)
    contrasena= models.CharField(max_length= 50)

    def __str__(self): 
        return str(self.nombre)

class Producto(models.Model):
    id_producto= models.AutoField(primary_key= True)
    precio= models.FloatField(max_length= 12)
    nombre_producto= models.CharField(max_length= 25)
    cantidad= models.IntegerField()
    categoria= models.ForeignKey('Categoria', on_delete= models.CASCADE, db_column='idCategoria')
    imagen= models.ImageField(upload_to='productos/', blank= True, null= True)

    def __str__(self): 
        return str(self.nombre_producto)

class Categoria(models.Model):
    id_categoria= models.AutoField(db_column='idCategoria', primary_key= True)
    nombre_categoria= models.CharField(max_length= 32)

    def __str__(self): 
        return str(self.nombre_categoria)
    
    