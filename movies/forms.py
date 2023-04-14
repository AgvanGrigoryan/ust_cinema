from django import forms
# from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from movies.models import Reviews, RatingStar, Rating


class ReviewForm(forms.ModelForm):
#     captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ('text', 'parent')
        widgets = {
            'text': forms.Textarea(attrs={"name": "text", "class": "form-control border", "id": "reviewText_input", "required": True}),
        }


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None)

    class Meta:
        model = Rating
        fields = ("star",)
        widgets = {
            "star": forms.RadioSelect(attrs={})
        }


