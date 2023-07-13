from .models import Film
from django.forms import ModelForm, TextInput, Textarea

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }