from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.forms import ReviewForm
from movies.models import Movie


class MoviesListView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'


class AddReview(View):

    def post(self, request, pk=None):
        print(request.POST)
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(pk=pk)
        if form.is_valid():
            form = form.save(commit=False)
            reviewParent = request.POST.get('reviewRapent', None)
            if reviewParent:
                form.parent_id = int(reviewParent)
            form.movie = movie
            form.author_id = request.user.id
            form.save()
        return redirect(movie.get_absolute_url())
