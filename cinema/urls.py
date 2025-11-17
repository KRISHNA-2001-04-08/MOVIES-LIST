from django.urls import path
from . import views

urlpatterns = [
    # existing HTML views
    path('', views.movie_list, name='movie_list'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:pk>/', views.update_movie, name='update_movie'),
    path('delete/<int:pk>/', views.delete_movie, name='delete_movie'),

    # REST API endpoints
    path('api/movies/', views.api_movie_list, name='api_movie_list'),
    path('api/movies/<int:pk>/', views.api_movie_detail, name='api_movie_detail'),
    path('api/movies/add/', views.api_add_movie, name='api_add_movie'),
    path('api/movies/update/<int:pk>/', views.api_update_movie, name='api_update_movie'),
    path('api/movies/delete/<int:pk>/', views.api_delete_movie, name='api_delete_movie'),
]
