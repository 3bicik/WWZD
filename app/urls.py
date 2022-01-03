from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('pred/', views.whole_predict),
    path('test_pred/', views.test_predict),
    path('json/', views.get_json),
    path('characters/', views.ListCharacters.as_view()),
    path('characters/<int:pk>/', views.DetailCharacter.as_view()),
]