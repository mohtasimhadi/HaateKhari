from django import forms
from .models import *

class KnowYourSelfForm(forms.ModelForm):
    class Meta:
        model = bodyPartsDetection
        fields = ['image']