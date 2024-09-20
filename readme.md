## Comandos usados en Django ##

* Django-admin startproject VHNGROUP #Crear proyecto con nombre VHNGROUP

* manage.py migrate #Crea una base de datos SQL lite con un templeate precragado. Migrar la base de datos nunca usarlo en produccion

* manage.py runserver #Ejecutar el servidor de desarrollo, nunca usarlo en produccion

* En el archivo settings.py cambiar el nombre el DEBUG a False cuando salgas de desarrollo

    * ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] #Selecciona que tipo de IPs se pueden acceder a la aplicacion

    * INSTALLED_APPS = Son las aplicaciones que se van a usar en la web

    * DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}} #Configuracion de la base de datos

    * LANGUAGE_CODE = 'en-us' #Configuracion de idioma

    * TIME_ZONE = 'UTC' #Configuracion de zona horaria

### Project and aplications ###
Django permite crear un proyecto que contenga varios aplicaciones. Cada aplicacion es un modulo que contiene diferentes funcionalidades.
* manage.py startapp blog #Para crear una aplicación se se debe indicar el nombre de la aplicacion
* Partes de una aplicacion
    * admin.py #Registra nuestro modelo en la administracion de Django
    * apps.py #Configuracion de la aplicacion
    * migrations #Archivos de migracion
    * models.py #Se definen las tables de nuestra bases de datos a traves de clases
    * tests.py #Se definen las pruebas de nuestra aplicacion
    * views.py #Se definen las vistas de nuestra aplicacion, se comunica con el modelo
### Models ###
Un modelo es una clase que representa una tabla de la base de datos.
En python podemos tener clases dentro de clases, por lo que podemos crear una clase que contenga otra clase.
#### Creamos una tabla de nombre Post. con las columnas title, slug y body ####
```
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, #Creamos una relacion con el modelo User
                                on_delete=models.CASCADE, #Al eliminar el usuaurio se eliminan todos los posts del usuario
                                related_name='blog_posts') # Desde la clase User se accede a todos los posts
    body = models.TextField()
    publish = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # status de la publicacion segun la clase Status
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT) 
    class Meta:
        ordering = ['-publish'] #Indicamos que va tener un ordenamiento inverso por fecha de publicacion
        indexes = [
            models.Index(fields=['-publish']),
        ]
    def __str__(self):
        return self.title
        ```

* Es importante activar las aplicaciones que se van a usar en la web, en el archivo settings.py en al seccion INSTALLED_APPS
* Para aplicar las migraciones se debe ejecutar el comando "manage.py makemigrations blog". se debe indicar el nombre de la aplicacion
* para verificar la consulta SQL se debe ejecutar el comando "manage.py sqlmigrate blog 0001" donde 0001 es el numero de la migracion antes creada
* Para confirmar la migración se debe ejecutar el comando "manage.py migrate"