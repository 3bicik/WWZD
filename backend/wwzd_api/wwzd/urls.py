from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCharacter.as_view()),
    path('<int:pk>/', views.DetailCharacter.as_view()),
    path('', views.ListLine.as_view()),
    path('<int:pk>/', views.DetailLine.as_view()),
]
