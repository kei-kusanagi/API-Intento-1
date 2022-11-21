En este ejercicio intentaremos recrear la api que hicimos en [DRF_Project](https://github.com/kei-kusanagi/DRF_Project) esto meramente como puro aprendizaje y acostumbrarme a crear API's de manera mas rápida


## INICIO

Comenzamos preparando una carpeta llamada "Intento 1" y comenzamos con lo basico, abrimos una terminal aquí y le damos ``git init`` para que nos cree un repositorio con git, luego creamos nuestro entorno virtual ``virtualenv -p python env`` y lo activamos ``.\env\Scripts\activate``

![[Pasted image 20221121104212.png]]

Ahora si, empezamos instalando Django y Django REST Framework ``pip install django djangorestframework`` (lo podemos hacer en una sola instrucción)

![[Pasted image 20221121104441.png]]


## Creacion del proyecto

Ahora creamos nuestro proyecto ``django-admin startproject watchmate .   `` (le ponemos el punto al final para que nos cree todos los archivos allí y no que cree otra carpeta llamada como el proyecto y dentro los archivos) luego creamos nuestra app (poniéndole un ``_app`` para que sea mas fácil de ver) ``python manage.py startapp watchlist_app`` y esta la declaramos en "settings.py"

![[Pasted image 20221121110248.png]]

Hacemos nuestras migraciones y creamos nuestro super usuario

![[Pasted image 20221121105851.png]]

Todo luce bien así que corramos el servidor ``python manage.py runserver``

![[Pasted image 20221121110016.png]]


Creemos nuestra carpeta "api" dentro de "watchlist_app" y dentro creemos nuestros 3 archivos principales "serlializers.py" "urls.py" y "views.py"

![[Pasted image 20221121111034.png]]


## Modelos


Ahora vamos a crear nuestros modelos en "watchlist_app/models.py" creare solamente la de plataformas para iniciar agregando y jugando un poco con estas

```Python
from django.db import models
  
class StreamPlataform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    def __str__(self):
        return self.name
```

Hacemos nuestras migraciones y luego vamos a "watchlist_app/admin.py" para agregar nuestro "StreamPlataform" a el panel de administración

(antes y despues)
![[Pasted image 20221121112745.png]]

Aquí directamente ya podemos agregar nuestras plataformas de streaming pero pues para eso no es una api, ósea no para agregarlas desde el panel de administración así que vallamos a crear nuestras "vistas", para esto necesitaremos "serializadores" y luego nuestras "urls"

## Views, Serializers and Url's

Ya le indicamos a la base de datos que usaremos los campos name, about y website para crear nuestras "StreamPlataform" ahora debemos decirle a nuestra app por medio de las vistas que hará con los campos que le pasemos, así que vamos a "watchlist_app/api/views.py" y agreguemos nuestra calss ``StreamPlataformVS`` haciendo nuestras importaciones, usaremos viewsets


```Python
from rest_framework import viewsets
  
from watchlist_app.models import StreamPlataform
  
class StreamPlataformVS(viewsets.ModelViewSet):
  
    queryset = StreamPlataform.objects.all()
    serializer_class = serializers.StreamPlataformSerializer
```

Aquí lo que estamos haciendo es crear nuestro método para formar el request que mandaremos pro el link, diciéndole que por el método ``viewsets`` (que ya trae todo lo que necesitamos para hacer CRUD) le asignaremos lo que es el ``queryset`` todos los objetos que obtengamos del modelo que hicimos previamente (osea name, about y website) luego eso los transformaremos gracias a nuestro serializador, pero este no lo hemos creado así que vallamos a "watchlist_app/api/serializers.py" y lo creamos

```Python
from rest_framework import serializers

from watchlist_app.models import StreamPlataform

  

class StreamPlataformSerializer(serializers.ModelSerializer):

    class Meta:

        model = StreamPlataform

        fields = "__all__"
```

Con el serializador recordemos que le estamos transformando los datos que obtengamos del modelo y los "traduciremos" pro así decirlo en formato Json, es como si fuera nuestro traductor y aquí también podremos declarar nuestras relaciones, pero primero hagamos que quede esto.

Nuestro siguiente paso es crear nuestra dirección a la cual enviaremos los request, así que vamos a "watchlist_app/api/urls.py"

```Python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views
  
router = DefaultRouter()
router.register('stream', views.StreamPlataformVS, basename='streamplataform')
  
urlpatterns = [
    path('', include(router.urls)),
]
```

Aquí tendremos que crear un router a fuerzas ya que el método que estamos usando "viewset" se basa en esto para poder obtener todos los métodos del CRUD

Pequeña anotación, para que tome en cuenta el ecosistema de Django REST Framework, tenemos que declararlo también dentro de nuestros "settings.py"

![[Pasted image 20221121140412.png]]

Por eso es que me estaba saliendo el error


Entonces, ya creamos nuestra url, chequemos que nos aparece en el explorador al ingresar al link http://127.0.0.1:8000/api/watch/stream/

![[Pasted image 20221121140507.png]]

Aquí tenemos ya alojado el método POST gracias a el enrutador y la "viewset" que le dimos, así que probemos pasándole este Json para crear una nueva plataforma

```Json
{
    "name": "Netflix",
    "about": "Most expensive Streaming Platform and popular",
    "website": "http://www.netflix.com"
}
```

Perfecto si nos dejo sin problemas

![[Pasted image 20221121141125.png]]