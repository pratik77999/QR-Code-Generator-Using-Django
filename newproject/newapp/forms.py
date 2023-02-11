from django import forms

class QRform(forms.Form):
    url=forms.URLField(label='Enter URL',widget=forms.URLInput(attrs={'class':'input-form','placeholder':'Enter URL here'}))
    name=forms.CharField(label='Enter QRcode Name',widget=forms.TextInput(attrs={'class':'input-form','placeholder':'Enter Name For Image'}))