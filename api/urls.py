from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('places/nearby', views.PlacesList.as_view()),
]
