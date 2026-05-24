from django.urls import path
from . import views

urlpatterns = [
    path('v3/', views.TarefaListCreate.as_view()),
    path('v3/<int:pk>/', views.TarefaDetail.as_view()),
]