from django.contrib import admin
from django.urls import path
from fakebook_panel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Ruta para la vista "login"
    path('error/', views.error_view, name='error'),  # Ruta para la vista de error
]
