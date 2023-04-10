from django.contrib.auth.decorators import login_required
from django.db.models import Q
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


class FilterMoviesView(ListView, GenreYear):

    def get_queryset(self):
        return movies_filter(self)


class JsonFilterMoviesView(ListView):
    def get_queryset(self):
        return movies_filter(self.request)

    def get(self, request, *args, **kwargs):

        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)

class AddStarRating(View):
    def get_client_ip(self, request):
        print(request.META)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            print(request.META.get('REMOTE_ADDR'))
            ip = request.META.get('REMOTE_ADDR')
        return ip

    @login_required
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
