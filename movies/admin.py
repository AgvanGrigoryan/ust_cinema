from django.contrib import admin

from movies.models import Movie, Category, Reviews, Genre, RatingStar, Actor, Rating, MovieShots

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)





