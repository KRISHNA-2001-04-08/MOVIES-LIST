from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer

def movie_list(request):
    query = request.GET.get('q')  # get search input
    if query:
        movies = Movie.objects.filter(
            Q(name__icontains=query) |
            Q(director__icontains=query) |
            Q(genre__icontains=query) |
            Q(year__icontains=query)
        )
    else:
        movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def add_movie(request):
    if request.method == "POST":
        name = request.POST['name']
        director = request.POST['director']
        year = request.POST['year']
        genre = request.POST['genre']
        Movie.objects.create(name=name, director=director, year=year, genre=genre)
        return redirect('movie_list')
    return render(request, 'add_movie.html')

def update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.name = request.POST['name']
        movie.director = request.POST['director']
        movie.year = request.POST['year']
        movie.genre = request.POST['genre']
        movie.save()
        return redirect('movie_list')
    return render(request, 'update_movie.html', {'movie': movie})

def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect('movie_list')
    return render(request, 'delete_movie.html', {'movie': movie})


@api_view(['GET'])
def api_movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def api_add_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def api_update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return Response({"message": "Movie deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
