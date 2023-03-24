from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.models import Movie


class MoviesListView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'
