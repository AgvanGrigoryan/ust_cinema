from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.models import Movie, Reviews


class MoviesListView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'


class AddReview(View):

    def post(self, request, pk):
        data = dict(request.POST)
        print(data)
        Reviews.objects.create(author_name=data['author_name'], email=data['email'], text=data['text'], movie=Movie.objects.get(pk=pk))
        print(request.POST)
        return redirect("movies")
