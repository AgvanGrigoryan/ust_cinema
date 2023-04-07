from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.forms import ReviewForm
from movies.logic import add_review, movies_filter
from movies.models import Movie, Actor, Genre


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values_list("year", flat=True).distinct()


class MoviesListView(GenreYear, ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(GenreYear, DetailView):
    model = Movie
    slug_field = 'url'


class AddReview(View):
    def post(self, request, pk=None):
        current_page = request.META.get('HTTP_REFERER')
        form = ReviewForm(request.POST)
        add_review(request, form, pk)
        return redirect(current_page)


class ActorView(GenreYear, DetailView):
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'id'


class FilterMoviesView(ListView, GenreYear):

    def get_queryset(self):
        return movies_filter(self)


class JsonFilterMoviesView(ListView):
    def get_queryset(self):
        return movies_filter(self.request)

    def get(self, request, *args, **kwargs):

        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)

