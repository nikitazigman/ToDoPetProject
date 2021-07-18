from django import forms

from .models import Task
from todo_list import settings


class TaskForm(forms.ModelForm):
    difficulty = forms.IntegerField(
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )
    
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'deadline',
            'difficulty',
            'status',
        ]
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
            }),
            'status': forms.CheckboxInput(attrs={
                'class': 'form-control',
            }),
        }
