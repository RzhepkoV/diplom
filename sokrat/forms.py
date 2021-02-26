from django import forms
from .models import Link


class LinkForm(forms.ModelForm):
    long = forms.TextInput()
    short = forms.CharField(label='Короткая ссылка', max_length=30)
    class Meta:
        model = Link
        fields = ['user', 'long', 'short']
        widgets = {
            'user': forms.HiddenInput(),
            'long': forms.Textarea(attrs={'rows': 1})
        }
