from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from movies.models import Movie, Category, Reviews, Genre, RatingStar, Actor, Rating, MovieShots


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


class MovieShotsAdminInline(admin.TabularInline):
    model = MovieShots
    fields = ('title', 'image_miniature', 'image')
    readonly_fields = ('title', 'image_miniature')

    extra = 0

    def image_miniature(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100px" max-height="600">')

    image_miniature.short_description = "Предпросмотр изображения"


class ReviewAdminInline(admin.StackedInline):
    model = Reviews
    fields = ('author', 'text')
    readonly_fields = ('author', 'text')

    extra = 0


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'url', 'draft')
    list_display_links = ('id', 'title')
    readonly_fields = ('id', 'poster_miniature')

    search_fields = ('title', 'category__name')
    search_help_text = 'Поиск по названию фильма, с учетом регистра.'
    save_on_top = True
    form = MovieAdminForm

    actions = ('publish', 'unpublish')
    list_filter = ('category', 'year')

    inlines = (MovieShotsAdminInline, ReviewAdminInline)
    list_editable = ('draft',)

    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'), 'description')
        }),
        ('Постер', {
            'fields': (('poster', 'poster_miniature'),)
        }),
        ('Жанр и Категория', {
            'fields': (('genres', 'category'),)
        }),
        ('Страна, год и год премьеры', {
            'fields': (('year', 'country', 'world_premiere'),)
        }),
        ('Актеры и Режиссеры', {
            'classes': ('collapse',),
            'fields': (('directors', 'actors'),)
        }),
        ('Бюджет и сборы', {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        ('Другое', {
            'fields': ('url', 'draft')
        })
    )

    def poster_miniature(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="100px" max-height="600">')

    poster_miniature.short_description = "Миниатюра постера"

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request=request, message=message_bit, level=2)

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change', )

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request=request, message=message_bit, level=2)

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change',)

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
class MovieShotsAdmin(admin.ModelAdmin):
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
    list_filter = ('movie__title',)
    readonly_fields = ('id',)
    search_fields = ('author__name',)
    search_help_text = 'Поиск по имени автора, с учетом регистра.'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'star', 'movie')
    list_display_links = ('id', 'ip')
    readonly_fields = ('id', 'ip')
    list_filter = ('ip', 'star')


admin.site.register(RatingStar)
