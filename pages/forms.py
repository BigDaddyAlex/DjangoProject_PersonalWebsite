from django import forms

class Contactform(forms.Form):
    fname=forms.CharField(label='Name')
    femail=forms.EmailField(label='Email')
    fmessage=forms.CharField(label='Message',widget=forms.Textarea)
