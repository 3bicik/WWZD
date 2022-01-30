from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('test_pred/', views.test_predict),
    path('s01e01/', views.s01e01),
    path('s01e02/', views.s01e02),
    path('s01e03/', views.s01e03),
    path('s01e04/', views.s01e04),
    path('s01e05/', views.s01e05),
    path('s01e06/', views.s01e06),
    path('s01e07/', views.s01e07),
    path('s01e08/', views.s01e08),
    path('s01e09/', views.s01e09),
    path('s01e10/', views.s01e10),
    path('s01e11/', views.s01e11),
    path('s01e12/', views.s01e12),
    path('s01e13/', views.s01e13),
    path('json/', views.get_json),
    path('characters/', views.ListCharacters.as_view()),
    path('characters/<int:pk>/', views.DetailCharacter.as_view()),
]