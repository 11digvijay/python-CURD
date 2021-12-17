from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = "__all__"
        widgets = {

            'company': forms.TextInput({'placeholder': 'company '}),
            'model_name': forms.TextInput({'placeholder': 'model_name'}),
            'ram': forms.TextInput({'placeholder': 'Ram in gb'}),
            'rom': forms.TextInput({'placeholder': 'Rom '}),
            'proc': forms.TextInput({'placeholder': 'processor'}),
            'price': forms.TextInput({'placeholder': 'price'}),
            'weight': forms.TextInput({'placeholder': ' weight'})
        }