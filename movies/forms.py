from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django import forms

from movies.models import Reviews, RatingStar, Rating


class ReviewForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3(
        attrs={
            'required_score': 0.85
        }
    ))

    class Meta:
        model = Reviews
        fields = ('text', 'parent', 'captcha')
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


