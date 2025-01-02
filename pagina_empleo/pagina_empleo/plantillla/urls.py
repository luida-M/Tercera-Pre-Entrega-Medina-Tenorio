"""
URL configuration for pagina_empleo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views import saludo, muestra_nombre
from pagina_empleo.views import pagina, dia_hoy, muestra_nombre, probando_template
#from App import Views
urlpatterns = [
    path("admin/", admin.site.urls),
    path ("inicio/", views.inicio)
    path("saludo/", saludo),
    path("dia_hoy/", dia_hoy),
    path("pagina/<nombre>/", muestra_nombre(nombre="algo")),
    path("nombre/<nombre>/", muestra_nombre),
    path("pagina/<nombre>/<numero>/", pagina),
    path("probando_template/", probando_template),
]