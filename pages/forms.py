from django import forms

class Contactform(forms.Form):
    fname=forms.CharField(label='Name')
    femail=forms.EmailField(label='Email')
    fmessage=forms.CharField(label='Message',widget=forms.Textarea)

class Topicform(forms.Form):
    topic_name=forms.CharField(label='Topic name')
    topic_TLDR=forms.CharField(label='TLDR')
    topic_body=forms.CharField(label='Topic body',widget=forms.Textarea)