from django import forms

class HashForm(forms.Form):
    text = forms.CharField(label='Enter text here', max_length=300)