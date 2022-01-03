from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('load/', views.load_data),
    path('pred/', views.test_predict),
    path('characters/', views.ListCharacters.as_view()),
    path('characters/<int:pk>/', views.DetailCharacter.as_view()),
    # path('lines/', views.ListLines.as_view()),
    # path('lines/<int:pk>/', views.DetailLine.as_view()),
]