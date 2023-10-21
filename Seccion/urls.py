from django.urls import path
from .views import *

urlpatterns = [
    path('Registrar/', Registrar.as_view(), name = "Registrar"),
    path('Iniciar/', Iniciar.as_view(), name = "Iniciar")
]