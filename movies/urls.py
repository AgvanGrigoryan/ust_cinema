from django.urls import path

from movies import views

urlpatterns = [
    path('', views.MoviesListView.as_view(), name='movies'),
    path(r'detail/<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail')

]
