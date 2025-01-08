# accounts/views.py
# views.py en la aplicación accounts
#def accounts_home_view(request):
#    return render(request, 'accounts/home.html')
# views.py en la aplicación accounts
from django.shortcuts import render
from accounts.models import User  # Importa el modelo 'User'
from accounts.forms import form # Importa el formulario 'UserForm' 

def accounts_home_view(request):
    return render(request, 'accounts/base.html')  # Asegúrate de que 'base.html' exista en 'templates/accounts/'

def base_view(request):
    return render(request, 'accounts/base.html')  # Vista para la base

def services_view(request):
    return render(request, 'accounts/servicios.html')  # Vista para 'servicios'

def portfolio_view(request):  # Corregido el nombre de 'porfolio_view' a 'portfolio_view'
    return render(request, 'accounts/vacantes.html')  # Vista para 'vacantes'

def about_view(request):
    return render(request, 'accounts/nosotros.html')  # Vista para 'nosotros'

def team_view(request):
    return render(request, 'accounts/clientes.html')  # Vista para 'clientes'

def contact_view(request):
    return render(request, 'accounts/contacto.html')  # Vista para 'contacto'

def user_formulario (request):
    print(request)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create(name=name, email=email, password=password)
        #user.save()
        return render(request, 'accounts/clientes.html', {'name': name, 'email': email, 'password': password})
    
    return render(request, 'accounts/formulario.html')  # Vista para 'formulario'

def form_con_api(request):
    if request.method == 'POST':
        mi_form = UserForm(request.POST)
        if mi_form.is_valid():
            informacion = mi_form.cleaned_data
            name = nombre(name=informacion['name'], email=informacion['email'], password=informacion['password'])       
        
            form.save()
            
            return render(request, 'accounts/clientes.html')
    else:
        mi_form = UserForm()
    return render(request, 'accounts/form_con_api.html', {'mi_form': mi_form})