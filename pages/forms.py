from django import forms

class Contactform(forms.Form):
    fname=forms.CharField(label='fname')
    femail=forms.CharField(label='femail')
    fmsg=forms.CharField(label='fmsg')
