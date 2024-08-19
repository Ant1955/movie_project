from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('films/', views.films, name='films'),
	path('add_films/', views.add_film, name='add_film')
]