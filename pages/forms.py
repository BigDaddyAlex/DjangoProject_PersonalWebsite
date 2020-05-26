from django import forms

class Contactform(forms.Form):
    fname=forms.CharField(label='name')
    femail=forms.EmailField(label='email')
    fmessage=forms.CharField(label='message',widget=forms.Textarea)
