from django.urls import path

from movies import views


urlpatterns = [
    path('', views.MoviesListView.as_view(), name='movies'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('filter/', views.FilterMoviesView.as_view(), name='filter'),
    path('json-filter/', views.JsonFilterMoviesView.as_view(), name='json_filter'),
    path('add-rating/', views.AddStarRating.as_view(), name='add_rating'),
    path('detail/<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/add', views.AddReview.as_view(), name="add_review"),
    path('actor/<int:pk>/', views.ActorView.as_view(), name="actor_detail"),

]

