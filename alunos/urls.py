from django.urls import path
from . import views

urlpatterns = [
    path('acessar_cadastro_alunos/',views.acessar_alunos),
    path('criar_evento/', views.criar_evento)

]