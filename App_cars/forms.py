from django import forms
from App_cars.models import CarModel, BlogModel, Review


class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        exclude = ['owner', 'selling_status']


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        exclude = ['writer', ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['buyer', ]

