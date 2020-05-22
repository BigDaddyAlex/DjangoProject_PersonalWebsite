from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Contactform

class homePageView(TemplateView):
    template_name = 'home.html'

class aboutPageView(TemplateView):
    template_name = 'about.html'

class thanksPageView(TemplateView):
    template_name = 'thanks.html'
 

class ContactView(FormView):
    template_name = 'contact.html'
    form_class=Contactform
    success_url='thanks/'


