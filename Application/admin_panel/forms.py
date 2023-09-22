from django import forms
from .models import AndroidApp

class AndroidAppForm(forms.ModelForm):
    class Meta:
        model = AndroidApp
        fields = '__all__'
