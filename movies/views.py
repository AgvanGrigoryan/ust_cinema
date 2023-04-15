from django.db.models.query import EmptyQuerySet
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.forms import ReviewForm, RatingForm
from movies.logic import add_review, movies_filter
from movies.models import Movie, Actor, Genre, Rating


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values_list("year", flat=True).distinct()


class MoviesListView(GenreYear, ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    paginate_by = 3


class MovieDetailView(GenreYear, DetailView):
    model = Movie
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        context["form"] = ReviewForm()
        return context


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


class FilterMoviesView(GenreYear, ListView):
    paginate_by = 2

    def get_queryset(self):
        return movies_filter(self.request)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['year'] = ''.join(f'year={x}&' for x in self.request.GET.getlist('year'))
        context['genre'] = ''.join(f'genre={x}&' for x in self.request.GET.getlist('genre'))
        return context


class JsonFilterMoviesView(ListView):
    def get_queryset(self):
        return movies_filter(self.request)

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)


class AddStarRating(View):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(self.request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class SearchView(GenreYear, ListView):
    paginate_by = 3
    def get_queryset(self):
        query = " ".join(self.request.GET.get('search-query').split()).lower()
        return Movie.objects.filter(title__icontains=query)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search_q'] = f"search-query={self.request.GET.get('search-query')}&"
        return context
