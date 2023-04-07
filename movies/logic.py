from movies.models import Movie


def add_review(request, form, pk):
    if form.is_valid():
        movie = Movie.objects.get(pk=pk)
        review_parent = request.POST.get('reviewRapent', None)
        form = form.save(commit=False)
        if review_parent:
            form.parent_id = int(review_parent)
        form.movie_id = movie.id
        form.author_id = request.user.id
        form.save()


def movies_filter(request):
    queryset = Movie.objects.all()
    if "year" in request.GET:
        queryset = queryset.filter(year__in=request.GET.getlist('year'))
    if "genre" in request.GET:
        queryset = queryset.filter(genres__in=request.GET.getlist("genre"))
    return queryset.distinct().values("title", "url", "poster")
