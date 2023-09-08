from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

# data = {'movies': [
#             {
#                 'id': 5,
#                 'title': 'Jaws',
#                 'Year': 1969,
#             },
#             {
#                 'id': 6,
#                 'title': 'Sharknado',
#                 'Year': 1980,
#             },
#             {
#                 'id': 7,
#                 'title': 'The Meg',
#                 'Year': 2018
#             }
#         ]
# }

def movies(request):
    data = Movie.objects.all()
    # Creating dictionary to be passed to template
    return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return render(request, 'movies/home.html')

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    
    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()

        return HttpResponseRedirect('/movies/')
    return render(request, 'movies/add.html')
    