from django import forms

class ResenaForm(forms.Form):
    name = forms.CharField(label='Su nombre', max_length=100)
    text = forms.CharField(label='Texto', widget=forms.Textarea)
    rating = forms.IntegerField(label='Estrellas', min_value=1, max_value=5)