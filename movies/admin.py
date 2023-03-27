from django.contrib import admin
from django.utils.safestring import mark_safe

from movies.models import Movie, Category, Reviews, Genre, RatingStar, Actor, Rating, MovieShots
from users.models import User


class ReviewAdminInline(admin.StackedInline):

    model = Reviews
    fields = ('author', 'text')
    readonly_fields = ('author', 'text')

    extra = 0


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'url', 'draft')
    list_display_links = ('id', 'title')
    readonly_fields = ('id',)

    search_fields = ('title', 'category__name')
    search_help_text = 'Поиск по названию фильма, с учетом регистра.'

    list_filter = ('category', 'year')

    inlines = (ReviewAdminInline,)
    list_editable = ('draft',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('id', 'name',)
    readonly_fields = ('id',)
    search_fields = ('name',)
    search_help_text = 'Поиск по названию категории, с учетом регистра.'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('id', 'name',)
    readonly_fields = ('id',)
    search_fields = ('name',)
    search_help_text = 'Поиск по названию жанра, с учетом регистра.'


@admin.register(MovieShots)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'movie', 'image_miniature')
    list_display_links = ('id', 'title')
    readonly_fields = ('id', 'image_miniature')
    search_fields = ('title',)
    search_help_text = 'Поиск по названию фрагмента, с учетом регистра.'

    list_filter = ('movie',)

    save_on_top = True

    def image_miniature(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50px" height="auto">')

    image_miniature.short_description = "Предпросмотр изображения"


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'image_miniature')
    list_display_links = ('id', 'name')
    readonly_fields = ('id', 'image_miniature')
    search_fields = ('name',)
    search_help_text = 'Поиск по имени Актера, с учетом регистра.'

    def image_miniature(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50px" height="auto">')
    image_miniature.short_description = "Предпросмотр изображения"

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'parent', 'movie')
    list_display_links = ('id', 'text')
    readonly_fields = ('id', 'author')
    search_fields = ('author__name',)
    search_help_text = 'Поиск по имени автора, с учетом регистра.'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'star', 'movie')
    list_display_links = ('id', 'ip')
    readonly_fields = ('id', 'ip')
    list_filter = ('ip', 'star')


admin.site.register(RatingStar)
