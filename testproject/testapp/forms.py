from django import forms
from django.db.models import fields
from .models import Bike


class BikeForm(forms.ModelForm):
    class Meta:     
        model = Bike
        fields = "__all__"

