from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.forms import ReviewForm
from movies.logic import add_review
from movies.models import Movie, Actor


class MoviesListView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'


class AddReview(View):
    def post(self, request, pk=None):
        current_page = request.META.get('HTTP_REFERER')
        form = ReviewForm(request.POST)
        add_review(request, form, pk)
        return redirect(current_page)


class ActorView(DetailView):
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'id'
