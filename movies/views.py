from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.forms import ReviewForm
from movies.models import Movie, Reviews


class MoviesListView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'

class AddReview(View):

    def post(self, request, pk=None):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(pk=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.author = request.user
            form.save()
        return redirect(movie.get_absolute_url())
