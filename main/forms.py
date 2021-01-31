from .models import Anketa
from django.forms import ModelForm, TextInput, Textarea


class AnketaForm(ModelForm):
    class Meta:
        model = Anketa
        fields = ["name", "surname", "about"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'u-border-1 u-border-white u-input u-input-rectangle',
                'placeholder': 'Имя',
            }),
            "surname": TextInput(attrs={
                'class': 'u-border-1 u-border-white u-input u-input-rectangle',
                'placeholder': 'Фамилия',
            }),
            "about": Textarea(attrs={
                'class': 'u-border-1 u-border-white u-input u-input-rectangle',
                'placeholder': 'О себе',
                'rows': '4'
            }),
        }

