from django.urls import path

from movies import views

urlpatterns = [
    path('', views.MoviesListView.as_view(), name='movies'),
    path('detail/<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/add', views.AddReview.as_view(), name="add_review")

]
