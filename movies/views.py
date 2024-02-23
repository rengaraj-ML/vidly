from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movies

# Create your views here.
def index(request):
    movies = Movies.objects.all()
    return render(request, 'movies\index.html', { 'movies': movies})
    
def detail(request, movie_id):
        movies = get_object_or_404(Movies, id=movie_id)
        return render(request, 'movies\detail.html', {'movies': movies})
    

