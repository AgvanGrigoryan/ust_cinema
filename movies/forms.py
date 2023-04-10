from django import forms

from movies.models import Reviews, RatingStar, Rating


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('text', 'parent')


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None)

    class Meta:
        model = Rating
        fields = ("star",)


