from django.urls import path
#from accounts import views
from . import views

urlpatterns = [
    path('', views.accounts_home_view, name='accounts_home'),
    path('base/', views.base_view, name='base'),  # Ruta para 'base'
    #ath('', views.services_view, name='home'),
    #path('', views.inicio_view),
    #path('servicios/', views.servicios),
    path('servicies/', views.services_view , name='services'), 
    path('portfolio/', views.portfolio_view, name='portfolio'), 
    path('about/', views.about_view, name='about'), 
    path('team/', views.team_view, name='team'), 
    path('contact/', views.contact_view, name='Contact'),
    path('formulario/', views.user_formulario, name='formulario'),
]

forms_html=[
    path('formulario/', views.user_formulario, name='formulario'),
]

forms_api=[
    path('form-con-api/', views.form_con_api, name='FormConApi'),
]
urlpatterns += forms_html + forms_api